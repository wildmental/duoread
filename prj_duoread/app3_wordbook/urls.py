"""
wordbook urls
"""
from django.urls import path
from . import views

app_name = 'wordbook'
urlpatterns = [
    path('', views.wordbook, name='wordbook'),
]
