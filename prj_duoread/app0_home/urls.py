"""
app home urls
"""
from django.urls import path
from app0_home import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
]
