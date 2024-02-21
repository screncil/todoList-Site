from django.shortcuts import render, HttpResponse
from .models import Users
from .database import checkUser, addUser

# Create your views here.




def login(request):
    if request.method == "POST":
        data = request.POST.dict()
        if checkUser(username=data['namefield'], password=data['passwordfield']):
            return HttpResponse("User logged in")
        else:
            return HttpResponse("Wrong password or username")

    else:
        return render(request, "Login/login.html")


def register(request):
    if request.method == "POST":
        data = request.POST.dict()
        if addUser(username=data['namefield'], password=data['passwordfield']):
            return HttpResponse("User successfully added!")
        else:
            return HttpResponse("Something went wrong!")
    else:
        return render(request, "Register/register.html")
