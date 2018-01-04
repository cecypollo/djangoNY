#URLS JOIN US

from django.conf.urls import url
from views import index, client_view, client_list, client_edit

urlpatterns = [
    url(r'^$', index, name='joinus'),
    url(r'^nuevo$', client_view, name='client_view'),
    url(r'^list$', client_list, name='client_list'),
    #url(r'^edit/(?P<id_client>\d+)/$', client_edit(), name='client_edit'),

]
