"""
app ______ urls
"""
from django.urls import path
from app7_dictionary import views

app_name = ''
urlpatterns = [
    path('cndic', views.DictCnView.as_view(), name='cndic'),
    path('endic', views.DictEnView.as_view(), name='endic'),
    # path('krdic', views.DictKrView.as_view(), name='krdic'),
]
