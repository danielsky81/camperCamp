from django.shortcuts import render, redirect, get_object_or_404, reverse, get_list_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Items, ItemComments, Votes
from .forms import ItemsForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages

def get_items(request):
    items = Items.objects.order_by('-created_date')
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
    
    return render(request, 'items.html', {'items': items, 'pages': pages, 'page_range': page_range})

def item_detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    item.views += 1
    item.save()
    return render(request, 'item_detail.html', {'item': item})


def create_or_edit_item(request, pk=None):
    item = get_object_or_404(Items, pk=pk) if pk else None
    if request.method == "POST":
        form = ItemsForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            item.author = request.user
            item.updated = True
            item.updated_date = timezone.now()
            item.save()
            return redirect(item_detail, item.pk)
    else:
        form = ItemsForm(instance=item)
    return render(request, 'itemform.html', {'form': form})

def add_comment_to_item(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.item = item
                comment.save()
                return redirect('item_detail', pk=item.pk)
        else:
            form = CommentForm()
    return render(request, 'item_commentform.html', {'form': form})

def edit_comment_item(request, pk):
    comment = get_object_or_404(ItemComments, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment.author = request.user
                comment.updated = True
                comment = form.save()
                return redirect('item_detail', comment.item.id)
        else:
            form = CommentForm(instance=comment)
    return render(request, 'item_commentform.html', {'form': form, 'comment': comment})

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
    if (request.user.is_authenticated and request.user != item.author):
        for vote in votes:
            if str(vote.user) == str(user) and str(vote.voted_item) == str(item):
                upvoted = True
    if upvoted is False:
        vote = Votes(voted_date=timezone.now(), user = user, voted_item = item)
        vote.save()
        item.votes += 1
        item.save()
        messages.success(request, 'Thank you for your vote!')
    else:
        messages.error(request, 'Thanks but you have already voted.')

    return redirect('item_detail', item.pk)
