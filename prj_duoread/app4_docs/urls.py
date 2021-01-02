"""
app docs urls
"""
from django.urls import path
from app4_docs import views

app_name = 'docs'
urlpatterns = [
    path('create/', views.DocCreate.as_view(), name='create'),
    path('list/', views.DocList.as_view(), name='list'),
    path('recent/', views.Recent.as_view(), name='recent'),
    path('update/', views.docs_update, name='update'),
]
