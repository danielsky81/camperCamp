from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from blog.models import PostComment
from items.models import Items, ItemComments, Votes
from accounts.models import Profile

def dashboard(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(username=request.user)
    blog_comments = PostComment.objects.filter(author=user).order_by('-created_date')
    issues = Items.objects.filter(author=user, item_type='issue').order_by('-created_date')
    issues_comments = ItemComments.objects.filter(author=user, item__item_type='issue').order_by('-created_date')
    features = Items.objects.filter(author=user, item_type='feature').order_by('-created_date')
    features_comments = ItemComments.objects.filter(author=user, item__item_type='feature').order_by('-created_date')
    issues_votes = Votes.objects.filter(user__username=request.user, voted_item__item_type='issue').order_by('-voted_date')
    features_votes = Votes.objects.filter(user__username=request.user, voted_item__item_type='feature').order_by('-voted_date')
    votes_count = Votes.objects.filter(user__username=request.user, voted_item__item_type='feature').count()
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'blog_comments': blog_comments, 'issues': issues, 'features': features, 'issues_comments': issues_comments, 'features_comments': features_comments, 'issues_votes': issues_votes, 'features_votes': features_votes, 'votes_count': votes_count, 'profile': profile})
    else:
        return redirect(reverse('hello'))

