#URLS JOIN US

from django.conf.urls import url
from views import index, insurance_view

urlpatterns = [
    url(r'^$', index, name='insurance'),
    url(r'^nuevo$', insurance_view, name='insurance_view'),
]
