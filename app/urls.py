from django.urls import path
from . import views

urlpatterns=[
    path('welcome/', views.welcome),
    path('welcome-template/', views.welcome_template),
]