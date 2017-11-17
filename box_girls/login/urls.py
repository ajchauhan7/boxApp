from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from views import custom_auth, do_logout


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='src/index.html'), name='home'),
    url(r'^loginpage/login/$', custom_auth, name='login'),
    url(r'^loginpage/$',auth_views.login, {'template_name': 'src/page-extra/user-login-3.html'}),
    url(r'^logout/$', do_logout, name='logout'),
]
