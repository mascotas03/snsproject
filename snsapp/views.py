from django.shortcuts import render

# Create your views here.

def signupfunc(request):
    return render(request, "signup.html",{"some":"shino"})  #templateとdataを組み合わせたものをレスポンスする