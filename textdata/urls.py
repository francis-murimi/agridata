from django.urls import path
from . import views

appname = 'textdata'

urlpatterns = [
    path('',views.home, name='home'),
    path('read/',views.read_file, name='read_file'),
    ]