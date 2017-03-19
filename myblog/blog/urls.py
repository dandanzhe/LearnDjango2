from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^pages/(?P<article_id>[0-9]+)/$',
        views.article_getpage, name='article_getpage'),
    url(r'^editpage/(?P<article_id>[0-9]+)/$',
        views.edit_page, name='editpage'),
    url(r'^editpage/act/$', views.edit_page_action, name='editpage_action'),
    url(r'^pages/delete/(?P<article_id>[0-9]+)/$',
        views.page_delete, name='article_delete'),
]
