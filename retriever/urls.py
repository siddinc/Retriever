from django.contrib import admin
from githubapi import views, forms
from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name = 'index'),
    path('githubapi/', include('githubapi.urls')),
    path('githubapi/', include('django.contrib.auth.urls')),
    path('thanks/', views.ThanksPageView.as_view(), name = 'thanks'),
]
