from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    return render(request,"login.html")


def login(request):
    return render(request,"main.html")





def customers(request):
    if request.method =="POST":
        return render(request,"customers.html")
    return render(request,"customers.html")






