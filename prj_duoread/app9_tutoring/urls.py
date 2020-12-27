"""
tutorboard urls
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.tutorboard),
    path('question_form/', views.add_tutor_req),
]
