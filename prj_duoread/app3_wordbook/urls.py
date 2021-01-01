"""
wordbook urls
"""
from django.urls import path
from app3_wordbook import views

app_name = 'wordbook'
urlpatterns = [
    path('', views.WordBookCn.as_view(), name='wordbook'),
    path('detail/<int:pk>/', views.WordDetail.as_view(), name='word_detail'),
    path('add/', views.WordAdd.as_view(), name='word_add'),
    path('mark_update/<int:pk>/', views.mark_update, name='mark_update'),
    path('memo_update/<int:pk>/', views.memo_update, name='memo_update'),
]
