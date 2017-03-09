
from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as authviews

urlpatterns = [

url(R'^$', views.post_list, name='post_list'),

]