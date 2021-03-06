"""perapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from perapp import settings
from django.views.generic.base import RedirectView


admin.site.site_title = 'WJ后台管理系统'
admin.site.site_header = 'WJ管理系统'

urlpatterns = [
    path('', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include("shopapp.urls")),
    path('favicon.ico', RedirectView.as_view(url=r'static/favicon.ico'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

