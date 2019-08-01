from django.shortcuts import render, redirect, get_object_or_404, reverse, get_list_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Issue, IssuesComment, Votes
from .forms import IssueForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages

def get_issues(request):
    issues = Issue.objects.order_by('-created_date')
    paginator = Paginator(issues, 4)
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
    
    return render(request, 'issues.html', {'issues': issues, 'items': items, 'page_range': page_range})

def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    issue.views += 1
    issue.save()
    return render(request, 'issue_detail.html', {'issue': issue})


def create_or_edit_issue(request, pk=None):
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            issue = form.save()
            issue.author = request.user
            issue.updated = True
            issue.updated_date = timezone.now()
            issue.save()
            return redirect(issue_detail, issue.pk)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issueform.html', {'form': form})

def add_comment_to_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.issue = issue
                comment.save()
                return redirect('issue_detail', pk=issue.pk)
        else:
            form = CommentForm()
    return render(request, 'issue_commentform.html', {'form': form})

def edit_comment_issue(request, pk):
    comment = get_object_or_404(IssuesComment, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment.author = request.user
                comment.updated = True
                comment = form.save()
                return redirect('issue_detail', comment.issue.id)
        else:
            form = CommentForm(instance=comment)
    return render(request, 'issue_commentform.html', {'form': form, 'comment': comment})

def delete_comment_issue(request, pk):
    comment = get_object_or_404(IssuesComment, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        comment.delete()
    return redirect('issue_detail', comment.issue.id)

def add_vote(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    votes = Votes.objects.filter(voted_issue=issue)
    user = User.objects.get(username=request.user)
    upvoted = False
    if (request.user.is_authenticated and request.user != issue.author):
        for vote in votes:
            if str(vote.user) == str(user) and str(vote.voted_issue) == str(issue):
                upvoted = True
    if upvoted is False:
        vote = Votes(voted_date=timezone.now(), user = user, voted_issue = issue)
        vote.save()
        issue.votes += 1
        issue.save()
        messages.success(request, 'Thank you for your vote!')
    else:
        messages.error(request, 'You have already voted on this issue.')

    return redirect('issue_detail', issue.pk)
