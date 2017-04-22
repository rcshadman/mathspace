from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',url(r'^dice$', views.dice, name='dice'),
)
