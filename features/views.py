from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Feature
from .forms import FeatureForm

def get_features(request):
    features = Feature.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    paginator = Paginator(features, 4)
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

    return render(request, 'features.html', {'features': features, 'items': items, 'page_range': page_range})

def feature_detail(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
    return render(request, 'feature_detail.html', {'feature': feature})


def create_or_edit_feature(request, pk=None):
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save()
            feature.author = request.user
            feature.save()
            return redirect(feature_detail, feature.pk)
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'featureform.html', {'form': form})