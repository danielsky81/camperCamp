from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from blog.models import PostComment
from items.models import Items, ItemComments

def dashboard(request):
    user = User.objects.get(username=request.user)
    blog_comments = PostComment.objects.filter(author=user).order_by('-created_date')
    items = Items.objects.filter(author=user).order_by('-created_date')
    items_comments = ItemComments.objects.filter(author=user).order_by('-created_date')
    # features = Feature.objects.filter(author=user).order_by('-created_date')
    # features_comments = CommentFeatures.objects.filter(author=user).order_by('-created_date')
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'blog_comments': blog_comments, 'items': items, 
        # 'features': features, 
        'items_comments': items_comments, 
        # 'features_comments': features_comments
        })
    else:
        return redirect(reverse('hello'))

