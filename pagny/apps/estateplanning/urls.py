#URLS JOIN US

from django.conf.urls import url
from views import index, estate_view

urlpatterns = [
    url(r'^$', index, name='estatep'),
    url(r'^nuevo$', estate_view, name='estate_view'),
]
