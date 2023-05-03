from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. 53dcc522 is the polls index.")


def Vista1(request):
    return render(request, "Vista1.html")

