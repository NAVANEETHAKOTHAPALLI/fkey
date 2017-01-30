
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^posts/$', views.PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
    url(r'^posts/(?P<pk>[0-9]+)/highlight/$', views.PostHighlight.as_view(),name='post-highlight'),
    url(r'^comments/$', views.CommentList.as_view(), name='comment-list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment-detail'),
    url(r'^comments/(?P<pk>[0-9]+)/highlight/$', views.CommentHighlight.as_view(),name='comment-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)