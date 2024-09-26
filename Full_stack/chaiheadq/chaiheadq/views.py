from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Home")
    return render(request,"start.html")