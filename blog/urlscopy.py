from django.conf.urls import include, url

from . import views

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),
    # url(r'^add/$', views.addPost, name='addPost'),
    # url(r'^(?P<post_id>[0-9]+)/modify/$', views.modifyPost, name='modifyPost'),
    # url(r'^(?P<post_id>[0-9]+)/delete/$', views.deletePost, name='deletePost'),
    # url(r'^(?P<post_id>[0-9]+)/comments/$', views.addComment, name='addComment'),
    # url(r'^comments/(?P<comment_id>[0-9]+)/reply/$', views.addComment, 'replyToComment'),
    url(r'^comments/(?P<comment_id>[0-9]+)/modify/$', views.modifyComment, 'modifyComment'),
    # url(r'^comments/(?P<comment_id>[0-9]+)/delete/$', views.deleteComment, 'deleteComment'),
]