from django.conf.urls import patterns, include, url
from django.contrib import admin
from agenda import views

urlpatterns = patterns('',
    url(r'^$', views.lista, name="lista"),
    url(r'^adiciona/$', views.adiciona, name="adiciona"),
)
