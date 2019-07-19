from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Feature
from .forms import FeatureForm

def get_features(request):
    features = Feature.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, 'features.html', {'features': features})

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