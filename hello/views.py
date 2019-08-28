from django.http import JsonResponse
from django.shortcuts import render
from items.models import Items
from django.db.models import Sum
from django.utils import timezone
from datetime import date, timedelta


def hello(request):
    issues = Items.objects.filter(item_type='issue')
    features = Items.objects.filter(item_type='feature')
    votes = Items.objects.aggregate(sum=Sum('votes'))
    total_issues = issues.count()
    total_features = features.count()
    top_voted_issues = issues.order_by('-votes')[:5]
    top_voted_features = features.order_by('-votes')[:5]
    top_view_issues = issues.order_by('-views')[:5]
    top_view_features = features.order_by('-views')[:5]

    data = []
    data_issues = []
    data_features = []
    items = Items.objects.all()
    for item in items:
        records = dict(
            id=item.id,
            item_type=item.item_type,
            category=item.category,
            views=item.views,
            votes=item.votes
        )
        data.append(records)
    for item in issues:
        records = dict(
            id=item.id,
            item_type=item.item_type,
            category=item.category,
            views=item.views,
            votes=item.votes
        )
        data_issues.append(records)
    for item in features:
        records = dict(
            id=item.id,
            item_type=item.item_type,
            category=item.category,
            views=item.views,
            votes=item.votes
        )
        data_features.append(records)

    now = int(timezone.now().timestamp())
    today = now - int(timedelta(days=1).total_seconds())
    week = now - int(timedelta(days=7).total_seconds())
    month = now - int(timedelta(days=30).total_seconds())

    updated_issues = [
        int(item['category_update'].timestamp()) for item in issues.values('category_update')
        if item['category_update'] is not None
    ]

    updated_features = [
        int(item['category_update'].timestamp()) for item in features.values('category_update')
        if item['category_update'] is not None
    ]

    daily_updated_issues = len(list(x for x in updated_issues if x in range(today, now)))
    weekly_updated_issues = len(list(x for x in updated_issues if x in range(week, now)))
    monthly_updated_issues = len(list(x for x in updated_issues if x in range(month, now)))

    daily_updated_features = len(list(x for x in updated_features if x in range(today, now)))
    weekly_updated_features = len(list(x for x in updated_features if x in range(week, now)))
    monthly_updated_features = len(list(x for x in updated_features if x in range(month, now)))

    categories_per_issues = [
        {'timespan': 'daily', 'value': daily_updated_issues},
        {'timespan': 'weekly', 'value': weekly_updated_issues},
        {'timespan': 'monthly', 'value': monthly_updated_issues}
    ]

    categories_per_features = [
        {'timespan': 'daily', 'value': daily_updated_features},
        {'timespan': 'weekly', 'value': weekly_updated_features},
        {'timespan': 'monthly', 'value': monthly_updated_features}
    ]

    return render(request, 'hello.html', {
        'total_issues': total_issues,
        'total_features': total_features,
        'votes': votes,
        'top_view_issues': top_view_issues,
        'top_view_features': top_view_features,
        'top_voted_issues': top_voted_issues,
        'top_voted_features': top_voted_features,
        'data': data,
        'data_issues': data_issues,
        'data_features': data_features,
        'categories_per_issues': categories_per_issues,
        'categories_per_features': categories_per_features
    })
