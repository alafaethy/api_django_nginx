from django.urls import path

from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('api/',views.api_views, name='api_view'),
    path('hellow/', views.hellow, name='hellow')
]