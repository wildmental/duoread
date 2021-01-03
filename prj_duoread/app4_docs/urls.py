"""
app docs urls
"""
from django.urls import path
from app4_docs import views

app_name = 'docs'
urlpatterns = [
    path('create/txt/', views.DocCreationTextView.as_view(), name='create_txt'),
    path('create/file/', views.DocCreationFileView.as_view(), name='create_file'),
    path('create/img/', views.DocCreationImageView.as_view(), name='create_img'),
    path('list/', views.DocList.as_view(), name='list'),
    path('recent/', views.Recent.as_view(), name='recent'),
    path('update/', views.docs_update, name='update'),
]
