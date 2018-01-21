from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^post/new/$', views.book_new, name='book_new'),
     url(r'^post/(?P<pk>\d+)/edit/$', views.book_edit, name='book_edit'),
]
