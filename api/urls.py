from django.urls import path
from .views import getUser
from . import views

urlpatterns = [
    path('', views.getUser),
    	path('register', views.UserRegister.as_view(), name='register'),

]
