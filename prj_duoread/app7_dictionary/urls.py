"""
app ______ urls
"""
from django.urls import path
from app7_dictionary import views

app_name = ''
urlpatterns = [
    path('', views.DictionaryCnView.as_view(), name='dictionary_cn'),
]
