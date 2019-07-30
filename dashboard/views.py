from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from blog.models import PostComment
from issues.models import Issue, IssuesComment
from features.models import Feature, CommentFeatures

def dashboard(request):
    user = User.objects.get(username=request.user)
    blog_comments = PostComment.objects.filter(author=user).order_by('-created_date')
    issues = Issue.objects.filter(author=user).order_by('-created_date')
    issues_comments = IssuesComment.objects.filter(author=user).order_by('-created_date')
    features = Feature.objects.filter(author=user).order_by('-created_date')
    features_comments = CommentFeatures.objects.filter(author=user).order_by('-created_date')
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'blog_comments': blog_comments, 'issues': issues, 'features': features, 'issues_comments': issues_comments, 'features_comments': features_comments})
    else:
        return redirect(reverse('hello'))

