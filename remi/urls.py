"""
URL configuration for remi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myapp import views
from myapp.views import diary,all_daily_log,daily_logs_by_date,add_daily_log

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/',diary),
    path('all_daily/',all_daily_log),
    path('daily_logs_by_date/<str:date>/', views.daily_logs_by_date, name='daily_logs_by_date'),
    path('all_daily_log/', views.all_daily_log, name='all_daily_log'),
    path('add_daily_log/', views.add_daily_log, name='add_daily_log')
]
