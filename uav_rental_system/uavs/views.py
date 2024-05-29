from django.shortcuts import render

def home(request):
    return render(request,"index.html")


def uavs(request):
    return render(request,"uavs.html")


