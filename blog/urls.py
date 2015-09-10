from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.PostView.as_view()), name='post'),
    url(r'^new/$', views.addPost, name='addPost'),
    url(r'^(?P<post_id>[0-9]+)/modify/$', views.modifyPost, name='modifyPost'),
    url(r'^(?P<post_id>[0-9]+)/delete/$', views.deletePost, name='deletePost'),
    url(r'^(?P<post_id>[0-9]+)/comments/$', views.addComment, name='postComment'),
    url(r'^comments/(?P<comment_id>[0-9]+)/reply/$', views.addComment, name='replyToComment'),
    url(r'^comments/(?P<comment_id>[0-9]+)/modify/$', views.modifyComment, name='modifyComment'),
    url(r'^comments/(?P<comment_id>[0-9]+)/delete/$', views.deleteComment, name='deleteComment'),
]