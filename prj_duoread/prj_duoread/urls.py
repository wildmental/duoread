"""prj_duoread URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # app urls
    path('', include('app0_home.urls')),
    path('account/', include('app1_user_accounts.urls')),
    path('setting/', include('app2_user_settings.urls')),
    path('wordbook/', include('app3_wordbook.urls')),
    path('docs/', include('app4_docs.urls')),

    path('tutorboard/', include('app9_tutoring.urls')),
]
