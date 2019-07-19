from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Issue
from .forms import IssueForm

def get_issues(request):
    issues = Issue.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, 'issues.html', {'issues': issues})

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