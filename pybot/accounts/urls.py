from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


urlpatterns=[
	path('register',views.register,name='register')
]