#URLS JOIN US

from django.conf.urls import url
from views import index, sigin_view

urlpatterns = [
    url(r'^$', index, name='signin'),
    url(r'^nuevo$', sigin_view, name='client_view'),
]
