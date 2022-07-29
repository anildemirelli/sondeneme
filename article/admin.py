from django.contrib import admin
from.models import Article, Comment  # models.py'ye gidip Article class ımızı ( modelimizi) aldık
# Register your models here.
# admin.site.register(Article) # Bu işlemle admin panelimizde Article'ımızı gösterdik !!


admin.site.register(Comment)



@admin.register(Article) # Üstteki yerine bu decorater ile kaydediyoruz ki özelleştirme yapalım
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    
    list_display_links = ["title", "created_date"] # Buda şu demek bunlara tıklandığında articleın linkine gidicek
    
    search_fields = ["title"]
    
    list_filter = ["created_date"]
    
    
    class Meta: # Bunu anlamaya gerek yok bu Djangonun verdiği özel bir class - Metadan baska bişe yazamayız
        model = Article #Bununla beraber Article'ı ArticleAdmine eşitliyoruz. 
