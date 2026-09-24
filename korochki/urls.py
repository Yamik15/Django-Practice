"""
URL configuration for korochki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path, include # include позволяет подключить файлы urls из отдельных приложений

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')), # Вход/Регистрация с префиксом /users/
    path('apps/', include('apps.applications.urls')), # Заявки и отзывы с префиксом /apps/
    path('', include('apps.core.urls')) # Главная - без префикса
]
