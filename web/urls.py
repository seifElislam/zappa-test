from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
     url(r'^login/$', views.login, name='login'),
     url(r'^messages/$', views.message_list),
     url(r'^messages/(?P<pk>[0-9]+)$', views.snippet_detail),
     url(r'^api-token/', auth_views.obtain_auth_token)
]