from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here. function based view

def signupfunc(request):
    if request.method == "POST":
        username2 = request.POST["username"]
        password2 = request.POST["password"]
        try:
            User.objects.get(username=username2)
            return render(request, "signup.html", {"error":"このユーザーは登録されています"})
        except:
            user = User.objects.create_user(username2, "", password2)
            return render(request, "signup.html",{"some":"shino"})  
    return render(request, "signup.html",{"some":"shino"})  #templateとdataを組み合わせたものをレスポンスする

def loginfunc(request):
    if request.method == "POST":
        username2 = request.POST["username"]
        password2 = request.POST["password"]
        user = authenticate(request, username=username2, password=password2)   #userの認証
        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            return redirect('login')
    return render(request, "login.html")

def listfunc(request):
    return render(request, "list.html") 