"""
app subscription urls
"""
from django.urls import path
from app10_subscription import views

app_name = 'subscription'
urlpatterns = [
    path('enroll/', views.enroll_view, name='enroll'),
    path('update/', views.update_view, name='update'),
]
