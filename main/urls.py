# myapp/urls.py
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('testWithoutIndex/', testWithoutIndex, name='testWithoutIndex'),
    path('testWithIndex/', testWithIndex, name = 'testWithIndex'),
    path('testWithPartIndex/', testWithPartIndex, name = 'testWithPartIndex'),
    path('testWithWrongIndex/', testWithWrongIndex, name = 'testWithWrongIndex'),
    path('withoutIndex/', GetDataWithoutIndex.as_view(), name='get_data_without'),
    path('withIndex/', GetDataWithIndex.as_view(), name = 'get_data_with'),
    path('withPartIndex/', GetDataWithPartIndex.as_view(), name = 'get_data_with_part'),
    path('withWrongIndex/', GetDataWithWrongIndex.as_view(), name = 'get_data_with_wrong') 
]
