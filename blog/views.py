from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, CommentBlog
from .forms import BlogPostForm, CommentForm


def get_posts(request):
    blog = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    paginator = Paginator(blog, 4)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'blog.html', {'blog': blog, 'items': items, 'page_range': page_range})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'post.html', {'post': post})


def create_or_edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                post.author = request.user
                post.save()
                return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'postform.html', {'form': form})
    else:
        return redirect(reverse('get_posts'))

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_superuser:
        post.delete()
    return redirect(reverse('get_posts'))

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
    return render(request, 'commentform.html', {'form': form})

def edit_comment_post(request, pk):
    comment = get_object_or_404(CommentBlog, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment.author = request.user
                comment = form.save()
                return redirect('post_detail', comment.post.id)
        else:
            form = CommentForm(instance=comment)
    return render(request, 'commentform.html', {'form': form, 'comment': comment})

def delete_comment_post(request, pk):
    comment = get_object_or_404(CommentBlog, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        comment.delete()
    return redirect(reverse('get_posts'))