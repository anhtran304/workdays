from django.urls import path

from . import views

app_name = 'workdays'
urlpatterns = [
    path('', views.index, name='index'),
    path('farmerportal/', views.farmerportal, name='farmerportal'),
    path('workerportal/', views.workerportal, name='workerportal'),
]