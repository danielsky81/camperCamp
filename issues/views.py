from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Issue, CommentIssues, Votes
from .forms import IssueForm, CommentForm
from django.contrib.auth.models import User

def get_issues(request):
    issues = Issue.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
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
    comment = get_object_or_404(CommentIssues, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment.author = request.user
                comment = form.save()
                return redirect('issue_detail', comment.issue.id)
        else:
            form = CommentForm(instance=comment)
    return render(request, 'issue_commentform.html', {'form': form, 'comment': comment})

def delete_comment_issue(request, pk):
    comment = get_object_or_404(CommentIssues, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author):
        comment.delete()
    return redirect(reverse('get_issues'))

def add_vote(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    user = User.objects.get(username=request.user)
    votes = Votes.objects.filter(vote=issue)
    votes_users = Votes.objects.filter(user=user)
    if request.user.is_authenticated:
        if request.user != issue.author:
            if request.user in votes_users:
                print('yes')
            # for vote in votes:
                # if str(vote) != str(user):
                #     issue_vote = get_object_or_404(Votes, vote=issue, user=request.user)        
                #     issue.votes += 1
                #     issue.save()
                #     issue_vote.vote = issue
                #     issue_vote.user = request.user
                #     issue_vote.save()
    return redirect('issue_detail', pk=issue.pk)