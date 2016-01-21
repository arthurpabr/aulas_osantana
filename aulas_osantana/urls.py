from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from agenda import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.lista, name="lista"),
    url(r'^adiciona/$', views.adiciona, name="adiciona"),
    url(r'^item/(?P<nr_item>\d+)/$', views.item, name="detalha"),
    url(r'^remove/(?P<nr_item>\d+)/$', views.remove, name="remove"),
    url(r'^login/$', login, {"template_name": "login.html"}, name="login"),
    url(r'^logout/$', logout_then_login, {"login_url": "/login/"}, name="logout"),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
