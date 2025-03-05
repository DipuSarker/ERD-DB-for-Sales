from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('setSessionData/', views.setSessionData, name='setSessionData'),
    path('getSessionData/', views.getSessionData, name='getSessionData'),
    path('clearSessionData/', views.clearSessionData, name='clearSessionData'),
    path('allSessionData/', views.allSessionData, name='allSessionData'),
]
