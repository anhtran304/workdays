from django.urls import path

from . import views

app_name = 'workdays'
urlpatterns = [
    path('', views.index, name='index'),
    path('farmerportal/', views.farmerportal, name='farmerportal'),
    path('workerportal/', views.workerportal, name='workerportal'),
    path("workerindex/", views.workerindex, name="workerindex"),
    path("farmerindex/", views.farmerindex, name="farmerindex"),
    path("workerpublic/", views.workerpublic, name="workerpublic"),
    path("farmerpublic/", views.farmerpublic, name="farmerpublic"),
    path("howitworks/", views.howitworks, name="howitworks"),
    path("about/", views.about, name="about"),
]