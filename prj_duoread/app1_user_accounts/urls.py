"""
UserAccounts urls
"""
from django.urls import path
from app1_user_accounts import views

app_name = 'user_accounts'
urlpatterns = [
    path('register/', views.register, name='register'),

    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),

    path('info/', views.userinfo, name='userinfo'),
    path('update/', views.ModelUpdateView.as_view(), name='update'),
]
