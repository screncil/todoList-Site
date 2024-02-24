from django.http import HttpResponse
from django.shortcuts import render, redirect
from Home.models import List
from Login.models import Users

from .Dependencies import checkFormAddTime

# Create your views here.



def index(request):
    if "session" in request.COOKIES:
        user = Users.objects.get(session_hash=request.COOKIES['session'])
        items = List.objects.filter(user_hash=request.COOKIES['session'])
        return render(request, "Home/index.html", {"user": user, "items": items, "lenitems": len(items)})
    else:
        return render(request, "Home/index.html", {"user": None})


def logout(request):
    response = redirect("/")
    response.delete_cookie("session")
    return response


def addItem(request):
    if request.method == "POST":
        data = request.POST.dict()
        if checkFormAddTime(deadline=data['date']):
            try:
                x = List(title=data['title'], description=data['description'], deadline=data['date'], user_hash=request.COOKIES['session'])
                x.save()
                return redirect('/')
            except Exception as ex:
                print(ex)
                return redirect('/')
        else:
            user = Users.objects.get(session_hash=request.COOKIES['session'])
            return render(request, "Home/addItem.html", {"user": user, "message": "Время не может быть меньше настоящего"})
    else:
        if "session" in request.COOKIES:
            user = Users.objects.get(session_hash=request.COOKIES['session'])
            return render(request, "Home/addItem.html", {"user": user, "message": ""})
        else:
            return redirect("/")
