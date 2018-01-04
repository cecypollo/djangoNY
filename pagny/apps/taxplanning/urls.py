#URLS JOIN US

from django.conf.urls import url
from views import index, tax_view

urlpatterns = [
    url(r'^$', index, name='taxp'),
    url(r'^nuevo$', tax_view, name='tax_view'),
]
