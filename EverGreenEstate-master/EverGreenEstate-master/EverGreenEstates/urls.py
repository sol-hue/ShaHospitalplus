
from django.contrib import admin
from django.urls import path
from EverGreenEstates import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agents'),
    path('contact/', views.cotact, name='contact'),
    path('', views.index, name='index'),
    path('properties/', views.properties, name='properties'),
    path('property-single/', views.property, name='property-single'),
    path('service-details/', views.service, name='service-details'),
    path('services/', views.services, name='services'),
    path('starter-page/', views.starter, name='starter-page'),

]

