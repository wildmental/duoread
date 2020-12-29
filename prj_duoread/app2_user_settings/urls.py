"""
app ______ urls
"""
from django.urls import path
from app2_user_settings import views

app_name = 'user_settings'
urlpatterns = [
    path('lang/', views.LangSet.as_view(), name='lang_init'),
    path('app/', views.AppSet.as_view(), name='app_setting'),
]
