# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', GetDataWithoutIndex.as_view(), name='get_data_without'),
    path('withIndex/', GetDataWithIndex.as_view(), name = 'get_data_with'),
    path('withPartIndex/', GetDataWithPartIndex.as_view(), name = 'get_data_with_part'),
    path('withWrongIndex/', GetDataWithWrongIndex.as_view(), name = 'get_data_with_wrong') 
]
