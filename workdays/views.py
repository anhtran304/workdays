from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def farmerportal(request):
    return render(request, "farmerportal.html")

def workerportal(request):
    return render(request, "workerportal.html")