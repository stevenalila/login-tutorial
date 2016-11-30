from django.conf.urls import url
from . import views

#we are adding a URL called /home
urlpatterns = [
	url(r'^$', views.home, name='home'),
]

