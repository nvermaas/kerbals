from django.conf.urls import url

from . import views

# setting the namespace
app_name = 'kerbals'

urlpatterns = [
    # /kerbals/
    #url(r'^$', views.index, name='index'),

    # /kerbals/
    url(r'^$', views.myIndexView.as_view(), name='index'),

    url(r'^list_basic$', views.list_basic, name='list_basic'),

    # /kerbals/list/
    url(r'^list/$', views.myListView.as_view(), name='list'),

    # /kerbals/h/<hike_id>/delete
    url(r'kerbal/(?P<pk>[0-9]+)/delete/$', views.myDeleteKerbal.as_view(), name='kerbal-delete'),

]