from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^(?P<num>\d+)$', views.landscape),
	url(r'^invalid_entry$', views.invalid)
]
