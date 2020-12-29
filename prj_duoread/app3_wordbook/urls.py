"""
wordbook urls
"""
from django.urls import path
from app3_wordbook import views

app_name = 'wordbook'
urlpatterns = [
    path('', views.wordbook, name='wordbook'),
    path('list/', views.WordList.as_view(), name='wordbook'),
    path('detail/<int:pk>/', views.WordDetail.as_view(), name='word_detail'),
    path('add/', views.WordAdd.as_view(), name='word_add'),
    path('update/<int:pk>/', views.WordUpdate.as_view(), name='word_update'),
]
