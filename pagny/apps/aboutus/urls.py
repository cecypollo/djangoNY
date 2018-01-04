#URLS JOIN US

from django.conf.urls import url
from views import index

urlpatterns = [
    url(r'^$', index, name='aboutus'),

]
