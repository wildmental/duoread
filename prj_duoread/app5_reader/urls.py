"""
app reader urls
"""
from django.urls import path
from app5_reader import views

app_name = 'reader'
urlpatterns = [
    path('doc=<int:doc>/p=<int:page>/w=<int:word>/',
         views.read_view, name='read'),
]
