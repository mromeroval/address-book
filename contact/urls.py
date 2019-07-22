from django.conf.urls import url
from . import views
 
 
urlpatterns = [
    url(r'^searchresult/$', views.contact_list_search, name="searchresult"),
    url(r'^activelist/$', views.contact_list_active, name="activelist"),
    url(r'^inactivelist/$', views.contact_list_inactive, name="inactivelist"),
    url(r'^create/$', views.create_contact, name="create"),
    url(r'^detail/(?P<id>\d+)/$', views.contact_detail, name="detail"),
    url(r'^edit/(?P<id>\d+)/$', views.edit_contact, name="edit"),
    url(r'^search/$', views.contact_search, name="search"),
]
