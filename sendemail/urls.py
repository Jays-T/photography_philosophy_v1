from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('success/', views.success, name='success'),
    path('emailsend/', views.emailsend, name='emailsend'),
]
