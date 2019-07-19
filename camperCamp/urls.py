"""camperCamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from hello import urls as hello_urls
from accounts import urls as accounts_urls
from dashboard import urls as dashboard_urls
from blog import urls as blog_urls
from .settings import MEDIA_ROOT
from contact import urls as contact_urls
from features import urls as features_urls
from issues import urls as issues_urls
from payment import urls as payment_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('hello.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/$', include('dashboard.urls')),
    url(r'^blog/', include('blog.urls')),
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^contact/', include('contact.urls')),
    url(r'^features/', include('features.urls')),
    url(r'^issues/', include('issues.urls')),
    url(r'^payment/', include('payment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)