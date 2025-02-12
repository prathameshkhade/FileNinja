"""
URL configuration for File_Ninja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from django.contrib import admin
from django.urls import path

from File_Ninja import views
from File_Ninja.views import google_login_redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('file-converter/', include('file_converter.urls')),
    path('file_manipulation/', include('file_manipulation.urls')),
    path('login/', views.login_view, name='login'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('google-login-redirect/', google_login_redirect, name='google_login_redirect'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('payment/', views.payment, name='payment'),

]


