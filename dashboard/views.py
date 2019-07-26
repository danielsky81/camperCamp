from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from blog.models import Comment
from issues.models import Issue
from features.models import Feature

def dashboard(request):
    user = User.objects.get(username=request.user)
    blog_comments = Comment.objects.filter(author=user).order_by('-published_date')
    issues = Issue.objects.filter(author=user).order_by('-published_date')
    features = Feature.objects.filter(author=user).order_by('-published_date')
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'blog_comments': blog_comments, 'issues': issues, 'features': features})
    else:
        return redirect(reverse('hello'))

