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
    path('testWithoutIndexLessRows/', testWithoutIndexLessRows, name = 'testWithoutIndexLessRows'),
    path('testWithIndexLessRows/', testWithIndexLessRows, name = 'testWithIndexLessRows'),
    path('testWithIndexBigCard/', testWithIndexBigCard, name = 'testWithIndexBigCard'),
    path('testWithPartIndexBigCard/', testWithPartIndexBigCard, name = 'testWithPartIndexBigCard'),
    path('testWithWrongIndexBigCard/', testWithWrongIndexBigCard, name = 'testWithWrongIndexBigCard'),

    path('withoutIndex/', GetDataWithoutIndex.as_view(), name='get_data_without'),
    path('withIndex/', GetDataWithIndex.as_view(), name = 'get_data_with'),
    path('withPartIndex/', GetDataWithPartIndex.as_view(), name = 'get_data_with_part'),
    path('withWrongIndex/', GetDataWithWrongIndex.as_view(), name = 'get_data_with_wrong'),
    path('withoutIndexLessRows/', GetDataWithoutIndexLessRows.as_view(), name = 'get_data_without_less'),
    path('withIndexLessRows/', GetDataWithIndexLessRows.as_view(), name = 'get_data_with_less'),
    path('withIndexBigCard/', GetDataWithIndexBigCard.as_view(), name = 'get_data_with_big'),
    path('withPartIndexBigCard/', GetDataWithPartIndexBigCard.as_view(), name = 'get_data_with_part_big'),
    path('withWrongIndexBigCard/', GetDataWithWrongIndexBigCard.as_view(), name = 'get_data_with_wrong_big')
]
