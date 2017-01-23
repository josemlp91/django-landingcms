from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'login/$', views.login_view, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'^home/edit/(?P<fieldtype>[-\w]+)/(?P<fieldname>[-\w]+)/$', views.home_cms_edit, name='home_cms_edit'),

]