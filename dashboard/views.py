from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from blog.models import PostComment
from items.models import Items, ItemComments

def dashboard(request):
    user = User.objects.get(username=request.user)
    blog_comments = PostComment.objects.filter(author=user).order_by('-created_date')
    issues = Items.objects.filter(author=user, item_type='issue').order_by('-created_date')
    issues_comments = ItemComments.objects.filter(author=user, item__item_type='issue').order_by('-created_date')
    features = Items.objects.filter(author=user, item_type='feature').order_by('-created_date')
    features_comments = ItemComments.objects.filter(author=user, item__item_type='feature').order_by('-created_date')
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'blog_comments': blog_comments, 'issues': issues, 
        'features': features, 
        'issues_comments': issues_comments, 
        'features_comments': features_comments
        })
    else:
        return redirect(reverse('hello'))

