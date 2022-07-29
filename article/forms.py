from django import forms
# https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
from .models import Article # Aynı klasördeki models.py dosyasından Article modelini aldık
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # burada modele eşitledik 
        fields = ["title","content", "article_image"]
        