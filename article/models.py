from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):  #Önce modelsin içindeki model modülünden kalıtım almamız lazım
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name= "Yazar") #Bununla bu alanımız aslında "user" tablosunu işareti ediyo diyoruz 
    # Eğer bir userimiz silinirse CASCADE sayesinde ona ait hersey hazır olan user tablomuzdan silinecek
    title = models.CharField(max_length=50, verbose_name="Başlık") # Başlığımızı simgeliceği için CharFielddan oluşturduk.
    #content = models.TextField(verbose_name="İçerik") # Normal text alanını kullandık
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True) # Bu şu demek biz herhangi bir veri eklediğimiz anda o anki tarihe bu created date'in içine atıcak
    article_image = models.FileField(blank = True, null = True, verbose_name="Makaleye Fotoğraf Ekleyin")
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments") #ilerde bir tane article aldıgımda Article.comments yaptıgımda bunun comment tablosuna erişebilirim. 
    comment_author = models.CharField(max_length=50, verbose_name="isim")
    comment_content = models.CharField(max_length=200, verbose_name="yorum")
    comment_date = models. DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content
    

    class Meta:
        ordering = ['-comment_date']