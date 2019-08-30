from django.shortcuts import render, redirect, get_object_or_404, reverse, get_list_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Items, ItemComments, Votes
from .forms import ItemsForm, CommentForm, CategoryForm
from django.contrib.auth.models import User
from django.contrib import messages


def get_items(request):
    item_type = ''
    if request.path == '/items/issues/':
        item_type = Items.objects.filter(item_type='issue').order_by('-created_date')
    elif request.path == '/items/features/':
        item_type = Items.objects.filter(item_type='feature').order_by('-created_date')
    tag = request.POST.get('tag')
    items = item_type
    if tag == 'all':
        items = item_type.order_by('-created_date')
    elif tag == 'new':
        items = item_type.filter(category='new')
    elif tag == 'to do':
        items = item_type.filter(category='to do')
    elif tag == 'in progress':
        items = item_type.filter(category='in progress')
    elif tag == 'done':
        items = item_type.filter(category='done')
    elif tag == 'rejected':
        items = item_type.filter(category='rejected')
    elif tag == 'require data':
        items = item_type.filter(category='require data')
    items_count = items.count()
    paginator = Paginator(items, 4)
    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pages = paginator.page(paginator.num_pages)

    index = pages.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'items.html', {
        'items': items,
        'pages': pages,
        'page_range': page_range,
        'items_count': items_count
    })


def item_detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    item.views += 1
    item.save()
    return render(request, 'item_detail.html', {'item': item})


def create_item(request, pk=None):
    item = get_object_or_404(Items, pk=pk) if pk else None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ItemsForm(request.POST, request.FILES, instance=item)
            if item is None:
                if form.is_valid():
                    item = form.save()
                    item.author = request.user
                    if request.path == '/items/issues/new/':
                        item.item_type = 'issue'
                    elif request.path == '/items/features/new/':
                        item.item_type = 'feature'
                    item.save()
                    return redirect('item_detail', pk=item.pk)
        else:
            if request.path == '/items/issues/new/':
                form = ItemsForm(instance=item, initial={'item_type': 'issue'})
            elif request.path == '/items/features/new/':
                form = ItemsForm(instance=item, initial={'item_type': 'feature'})
        return render(request, 'itemform.html', {'form': form, 'item': item})
    else:
        return redirect(reverse('hello'))


def edit_item(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.user.is_authenticated and request.user == item.author:    
        if request.method == 'POST':
            form = ItemsForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                item.updated_date = timezone.now()
                item.save()
                return redirect('item_detail', pk=item.pk)
            else:
                return redirect(reverse('hello'))
        else:
            form = ItemsForm(instance=item)
        return render(request, 'itemform.html', {'form': form, 'item': item})
    else:
        return redirect(reverse('hello'))



def add_comment_to_item(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.item = item
                comment.save()
                return redirect('item_detail', pk=item.pk)
        else:
            form = CommentForm()
    return render(request, 'item_commentform.html', {
        'form': form,
        'item': item.item_type
    })


def edit_comment_item(request, pk):
    comment = get_object_or_404(ItemComments, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment.updated_date = timezone.now()
                comment = form.save()
                return redirect('item_detail', comment.item.id)
        else:
            form = CommentForm(instance=comment)
    return render(request, 'item_commentform.html', {
        'form': form,
        'comment': comment
    })


def delete_comment_item(request, pk):
    comment = get_object_or_404(ItemComments, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        comment.delete()
    return redirect('item_detail', comment.item.id)


def add_vote(request, pk):
    item = get_object_or_404(Items, pk=pk)
    votes = Votes.objects.filter(voted_item=item)
    user = User.objects.get(username=request.user)
    upvoted = False
    if item.item_type == 'issue':
        if (request.user.is_authenticated and request.user != item.author):
            for vote in votes:
                if str(vote.user) == str(user) and str(vote.voted_item) == str(item):
                    upvoted = True
    if upvoted is False and item.item_type == 'issue':
        vote = Votes(
            voted_date=timezone.now(),
            user=user,
            voted_item=item
        )
        vote.votes_number = 1
        vote.save()
        item.votes += 1
        item.save()
        messages.success(request, 'Thank you for your vote!')
    elif item.item_type == 'feature':
        votes_number = int(request.POST.get('votes_number'))
        request.session['feature'] = item.id
        request.session['votes_number'] = votes_number
        return redirect('checkout', item.pk)
    else:
        messages.error(request, 'Thanks but you have already voted.')

    return redirect('item_detail', item.pk)


def admin_update(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CategoryForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                item = form.save()
                item.category_update = timezone.now()
                item.save()
                return redirect(item_detail, item.pk)
        else:
            form = CategoryForm(instance=item)
        return render(request, 'category_update.html', {
            'form': form,
            'item': item
        })
    else:
        return redirect('item_detail', item.pk)
