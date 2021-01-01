"""
app reader urls
"""
from django.urls import path
from app5_reader import views

app_name = 'reader'
urlpatterns = [
    path('', views.read_view, name='read'),
]
