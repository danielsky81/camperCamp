from django.http import JsonResponse
from django.shortcuts import render
from items.models import Items
from django.db.models import Sum

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
    items = Items.objects.all()
    for item in items:
        json_obj = dict(id = item.id, item_type = item.item_type, category = item.category, views = item.views, votes = item.votes)
        data.append(json_obj)
    print(data)
    return render(request, 'hello.html', {'total_issues': total_issues, 'total_features': total_features, 'votes': votes, 'top_view_issues': top_view_issues, 'top_view_features': top_view_features, 'top_voted_issues': top_voted_issues, 'top_voted_features': top_voted_features, 'data': data})

def get_data(request):
    data = []
    items = Items.objects.all()
    for item in items:
        json_obj = dict(id = item.id, item_type = item.item_type, category = item.category, views = item.views, votes = item.votes, created_date = item.created_date)
        data.append(json_obj)
    return JsonResponse(data, safe=False)