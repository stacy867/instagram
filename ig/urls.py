from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^new/comment/(\d+)$', views.new_comment, name='new-comment'),
    # url(r'^comment/(\d+)/$', views.comment, name='comment'),
    # url(r'^comment/(?P<image_id>\d+)', views.new_comment, name='new-comment'),
    url(r'^new/newprofile$', views.new_profile, name='new-profile'),
    url(r'^new/profile$', views.profile, name='profile'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'^likes/(?P<id>\d+)',views.likes,name ='like'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)