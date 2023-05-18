from django.urls import path, re_path
from .views import PostListView, post_detail, post_share

app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', PostListView.as_view(), name='post_list_by_tag'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$', post_detail,
        name='post_detail'),

    path('<post_id>/share/', post_share, name='post_share'),
]