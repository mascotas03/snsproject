from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username, "", password)
        print("this is post method")
        print(request.POST)
    else:
        print("this is not post method")
    return render(request, "signup.html",{"some":"shino"})  #templateとdataを組み合わせたものをレスポンスする