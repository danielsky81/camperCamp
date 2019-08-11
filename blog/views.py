from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, PostComment
from .forms import BlogPostForm, BlogCommentForm


def get_posts(request):
    blog_tags = ''
    # Filter objects by tag
    if request.path == '/blog/':
        blog_tags = Post.objects.order_by('-created_date')
    elif request.path == '/blog/tag_issues/':
        blog_tags = Post.objects.filter(tag='issue')
    elif request.path == '/blog/tag_features/':
        blog_tags = Post.objects.filter(tag='feature')
    elif request.path == '/blog/tag_news/':
        blog_tags = Post.objects.filter(tag='news')
    elif request.path == '/blog/tag_other/':
        blog_tags = Post.objects.filter(tag='other')
    blog = blog_tags.order_by('-created_date') 
    blog_count = blog.count()
    paginator = Paginator(blog, 4)
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

    return render(request, 'blog.html', {'blog': blog, 'pages': pages, 'page_range': page_range, 'blog_count': blog_count})


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
            if post == None:
                if form.is_valid():
                    post = form.save()
                    post.author = request.user
                    post.save()
                    return redirect(post_detail, post.pk)
            elif post != None:
                if form.is_valid():
                    post.updated_date = timezone.now()
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
            form = BlogCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = BlogCommentForm()
    return render(request, 'commentform.html', {'form': form})

def edit_comment_post(request, pk):
    comment = get_object_or_404(PostComment, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        if request.method == 'POST':
            form = BlogCommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment.author = request.user
                comment.updated_date = timezone.now()
                comment = form.save()
                return redirect('post_detail', comment.post.id)
        else:
            form = BlogCommentForm(instance=comment)
    return render(request, 'commentform.html', {'form': form, 'comment': comment})

def delete_comment_post(request, pk):
    comment = get_object_or_404(PostComment, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        comment.delete()
    return redirect(reverse('get_posts'))