from . import views
from django.conf.urls import url

app_name = 'core'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^autores/$', views.author_list, name='author_list'),
    url(r'^autor/(?P<pk>\d+)/$', views.author_detail, name='author_detail'),
    url(r'^novo-autor/$', views.author_create, name='author_add'),
    url(r'^autor/(?P<pk>\d+)/editar/$', views.author_edit, name='author_edit'),
    url(r'^autor/(?P<pk>\d+)/apagar/$', views.author_delete, name='author_delete'),
]
