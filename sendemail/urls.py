from django.urls import path

from . import views

urlpatterns = [
    path('emailsend/', views.emailsend, name='emailsend'),
]
