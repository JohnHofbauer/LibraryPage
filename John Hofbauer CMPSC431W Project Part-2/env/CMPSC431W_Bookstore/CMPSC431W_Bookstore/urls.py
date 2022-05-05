"""CMPSC431W_Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include

# Imports the views.py function.
from bookstore.views import *


# Ties the function to an actual URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include("django.contrib.auth.urls")),
    path('upload-csv/', content_upload, name="content_upload"),
    path('results/', search_results, name="search_results"),
    path('login/', loginpage, name="loginpage"),
    path('register/', register, name="register"),
    path('searchresults/', search_results, name="search_results"),
    path('accounts/profile/', accountprofile, name="accountprofile"),
    path('order/', order, name="order"),
    path('companyView/', companyView, name="companyView"),
    path('Users/', Users, name="Users"),
]
