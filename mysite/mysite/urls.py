from django.contrib import admin
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.homeView, name='homeView'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', include('notes.urls')),
]
