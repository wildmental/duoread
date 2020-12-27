"""
UserAccounts urls
"""
from django.urls import path
from app1_user_accounts import views

app_name = 'user_accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
