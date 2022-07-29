from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    #path('create/', views.index, name = "index"),
    path('dashboard/', views.dashboard, name = "kontrolPaneli"),
    path('addarticle/', views.addArticle, name = "makaleEkle"),
    path('article/<int:id>', views.detail, name = "detay"),
    path('update/<int:id>', views.updateArticle, name = "güncelle"),
    path('delete/<int:id>', views.deleteArticle, name = "sil"),
    path('', views.articles, name = "makaleler"),
    path('comment/<int:id>', views.addComment, name = "yorumEkle"),
]   
