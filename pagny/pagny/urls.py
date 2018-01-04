"""pagny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('apps.main.urls', namespace="main")),
    url(r'^joinus/', include('apps.joinus.urls', namespace="joinus")),
    url(r'^learnmore/', include('apps.learnmore.urls', namespace="learnmore")),
    url(r'^aboutus/', include('apps.aboutus.urls', namespace="aboutus")),
    url(r'^demo/', include('apps.demo.urls', namespace="demo")),
    url(r'^dashboard/', include('apps.dashboard.urls', namespace="dashboard")),
    url(r'^insurance/', include('apps.insurance.urls', namespace="insurance")),
    url(r'^signin/', include('apps.signin.urls', namespace="signin")),
    url(r'^tax/', include('apps.taxplanning.urls', namespace="tax")),
    url(r'^estate/', include('apps.estateplanning.urls', namespace="estate")),

]
