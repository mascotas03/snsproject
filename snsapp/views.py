from django.shortcuts import render
from django.contrib.auth.models import User

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
            return render(request, "signup.html",{"some":"shino"})  #templateとdataを組み合わせたものをレスポンスする
    return render(request, "signup.html",{"some":"shino"})  #templateとdataを組み合わせたものをレスポンスする