from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^addnote/$', views.addnote, name='addnote'),
    url(r'^viewnotes/$', views.ListNotes.as_view(), name='viewnotes'),
    url(r'^updatenote/(?P<pk>\d+)/$',
        views.UpdateNotes.as_view(), name='updatenote'),
    url(r'^deletestatus/(?P<pk>\d+)/$',
        views.onDeleteStatus, name='deletestatus'),
    url(r'^readstatus/(?P<pk>\d+)/$',
        views.onReadStatus, name='readstatus'),
]
