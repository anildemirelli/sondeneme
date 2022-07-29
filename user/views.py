from django.shortcuts import render, redirect
from pyparsing import autoname_elements
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def register(request):

    form = RegisterForm(request.POST or None) # bununla beraber hem post hem get durumunu alıyoruz.
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla kayıt oldunuz. ")                   
        return redirect("anasayfa")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)
    """form = RegisterForm()
    context = {
        "form" : form
    }
    return render(request, "register.html", context)"""

def loginUser(request):
    if not request.user.is_authenticated:
        
        form = LoginForm(request.POST or None)

        context = {
            "form":form
        }

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username,password = password)

            if user is None: # kullanıcı bulunmazsa user boş döncek 
                messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
                return render(request,"login.html",context)

            messages.success(request,"Başarıyla Giriş Yaptınız")
            login(request,user)
            return redirect("anasayfa")
    else:
        messages.warning(request,"Zaten giriş yaptınız !")
        return redirect("anasayfa")
    return render(request,"login.html",context)   

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış yaptınız..")
    return redirect("anasayfa")

