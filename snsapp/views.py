from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from . models import SnsModel
from django.contrib.auth.decorators import login_required

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
            return render(request, "list.html")  
    return render(request, "signup.html")  #templateとdataを組み合わせたものをレスポンスする

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

def logoutfunc(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')

@login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    return render(request, "list.html", {"object_list": object_list}) 