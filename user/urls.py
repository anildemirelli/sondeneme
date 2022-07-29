from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.register, name = "kayıt"),
    path('login/', views.loginUser, name = "giris"),
    path('logout/', views.logoutUser, name = "cikis"),
    
]