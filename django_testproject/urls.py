"""django_testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from login import views as login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('login/', include('login.urls')),
    path('', login_view.show_home,name='home'),
    path('app/', login_view.show_app_screen,name='app'),
    path('cracked/get_featured', login_view.feature_user,name='feature_user'),
    path('submitkey', login_view.submit_key_screen,name="submit_key_screen"),
    path('submitkeyvalue', login_view.submit_key,name="submit_key"),
    path('getfeatured', login_view.get_featured,name="get_featured"),
    path('solved_by', login_view.solved_by,name="solved_by"),

    
]
