from django.shortcuts import render
from django.http import HttpResponse

def services(request):
    return render(request,'services.html')

# Create your views here.
