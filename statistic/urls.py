from django.urls import path
from . import views

# app_name='statistic'

urlpatterns=[
    path('', views.index, name='index'),
]