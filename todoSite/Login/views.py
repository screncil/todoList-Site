from django.shortcuts import render, HttpResponse, redirect
from .models import Users
from .database import checkUser, addUser
from .Encryption import Encrypt

# Create your views here.


crypto_ = Encrypt()

def login(request):
    if request.method == "POST":
        data = request.POST.dict()
        if checkUser(username=data['namefield'], password=crypto_.encrypt(data['passwordfield'])):
            response = redirect("/")
            user = Users.objects.get(username=data['namefield'])
            response.set_cookie("session", user.session_hash)
            return response 
        else:
            return HttpResponse("Wrong password or username")

    else:
        if not "session" in request.COOKIES:
            return render(request, "Login/login.html")
        else:
            return redirect("/")


def register(request):
    if request.method == "POST":
        data = request.POST.dict()
        hash = crypto_.generate_hash()
        if addUser(username=data['namefield'], password=crypto_.encrypt(data['passwordfield']), session_hash=hash):
            return redirect("/login")
        else:
            return HttpResponse("Something went wrong!")
    else:
        if not "session" in request.COOKIES:
            return render(request, "Register/register.html")
        else:
            return redirect("/")
