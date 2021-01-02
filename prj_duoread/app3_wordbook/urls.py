"""
wordbook urls
"""
from django.urls import path
from app3_wordbook import views

app_name = 'wordbook'
urlpatterns = [
    path('', views.WordBookCn.as_view(), name='wordbook'),
    path('detail/<int:pk>/', views.WordDetail.as_view(), name='word_detail'),
    path('read_add/', views.reader_word_add, name='reader_word_add'),
    path('dic_add/', views.dic_word_add, name='dic_word_add'),
    path('mark_update/<int:pk>/', views.mark_update, name='mark_update'),
    path('memo_update/<int:pk>/', views.memo_update, name='memo_update'),
]
