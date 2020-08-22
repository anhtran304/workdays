from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def farmerportal(request):
    return render(request, "farmerportal.html")

def workerportal(request):
    return render(request, "workerportal.html")

def workerindex(request):
    return render(request, "workerindex.html")

def farmerindex(request):
    return render(request, "farmerindex.html")

def farmerpublic(request):
    return render(request, "farmerpublic.html")

def workerpublic(request):
    return render(request, "workerpublic.html")

def howitworks(request):
    return render(request, "howitworks.html")