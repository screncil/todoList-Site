from django.http import HttpResponse
from django.shortcuts import render
from Home.models import List
import time

# Create your views here.



def index(request):
    return render(request, "Home/index.html")
