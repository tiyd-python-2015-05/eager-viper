"""eager_viper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from activity.views import ActivityViewSet, StatsView, StatView

router = DefaultRouter(trailing_slash=False)
router.register('activities', ActivityViewSet, base_name='activity')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/activities/(?P<activity_pk>\d+)/stats', StatsView.as_view(), name="stats"),
    url(r'^api/stats/(?P<pk>\d+)', StatView.as_view(), name="stat-detail"),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
