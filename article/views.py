from django import views
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.urls import reverse
from flask import url_for
import article
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})



def index(request):
    kontext = {
        "number1" : 10,
        "number2" : 20,
        "number3" : 30
    }
    #return HttpResponse("Anasayfa") # Buraya istersek html de dönebiliriz. ( <h3>Anasayfa</h3>) şeklinde   
    #return render(request, "index.html") # Bu şekilde de direk templateleri dönebiliriz.. 
    #return render(request, "index.html", {"number" : 7}) # istersek bu sekilde context gönderebiliriz
    return render(request,"index.html", kontext) # yada şeklinde direk değişken gönderebiliriz 
def about(request):
    return render(request, "about.html")

@login_required(login_url='user:giris')
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url='/')
def addArticle(request):
    #form = ArticleForm(request.POST or None)
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article_objesi = form.save(commit=False) #Commit = False komutunu ekleyerek dur sen kaydetme ben yapcam diyoruz. 
        
        article_objesi.author = request.user
        article_objesi.save()
        
        messages.success(request, "Makale Başarıyla oluşturuldu")
        return redirect("anasayfa")
    return render(request,"addarticle.html", {"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id = id)
    
    comments = article.comments.all()
    return render(request, "detail.html", {"article":article, "comments":comments})


@login_required
def updateArticle(request,id):
    article = get_object_or_404(Article, id=id)
    
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False) #Commit = False komutunu ekleyerek dur sen kaydetme ben yapcam diyoruz. 
        
        article.author = request.user
        article.save()
        
        messages.success(request, "Makale Başarıyla güncellendi")
        return redirect("anasayfa")
    return render(request, "update.html", {"form" : form})


@login_required
def deleteArticle(request,id):
    article = get_object_or_404(Article, id = id)
    
    article.delete()
    messages.success(request, "Makale Başarıyla silindi...")
    return redirect("article:kontrolPaneli")


def addComment(request,id):
    article = get_object_or_404(Article, id = id) # article get objeclte alıyoruz içine article modelini gönderiyoruz ve id si id olan post methodu alıyoruz. 
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author") # içindeki değişken detail sayfasındaki inputun name i
        comment_content = request.POST.get("comment_content") 

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()
        return redirect(reverse("article:detay", kwargs={"id":id} ))
    #/articles/detail/15   ustteki formül buna çevirdi. 

def deneme(request):
    return render(request, "boş.html")