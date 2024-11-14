
from django.urls import path
from . import views

app = 'transport'
urlpatterns = [
    path('', views.containers, name='containers'),
    path('check/', views.check, name='check'),
]