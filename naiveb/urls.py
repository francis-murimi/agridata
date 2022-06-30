from django.urls import path
from . import views

appname = 'naiveb'

urlpatterns = [
    path('get-link/',views.get_link,name='get_link'),
    path('get-text/<id>/', views.get_text, name='get_text'),
    path('classify/<id>/',views.classify, name='classify'),
    path('results/<id>/',views.results, name='results'),
    ]