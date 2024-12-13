from django.shortcuts import render,HttpResponse,redirect
from warehousemgt.models import *
from .forms import MyForm




# Create your views here.


def index(request):
    return render(request,"login.html")


def login(request):
    data = {"all_items": Item.objects.all()}
    return render(request,"main.html",data)


def customers(request):
    if request.method =="POST":
        return render(request,"customers.html")
    return render(request,"customers.html")



def add_item(request):
    
    if request.method == 'GET':
        return render(request,"add_item.html")
    
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            name_item = request.POST.get("Item_name")
            sn = request.POST.get("Item_SN")
            description = request.POST.get("description")
            document = Document.objects.create(file=file, title=name_item)
            new_item = Item.objects.create(
                name_item=name_item,
                icon=document,
                sn=sn,
                description=description,
            )
            return redirect("/login") 
        else:
            return render(request, "add_item.html", {"form": form})
        
        
def delete_item(request):
    delete_item = request.POST["item_id"]
    item = Item.objects.get(id=int(delete_item))
    item.delete()

    return redirect("/login")
    
    
    
def edit_item(request):
        form = MyForm(request.POST, request.FILES)
        item = request.POST["item_id"]
        # edit_item = Item.objects.get(id=int(item))
        
        print(item)
        return redirect("/login") 
        
        # if form.is_valid():
        #     file = form.cleaned_data['file']
        #     name_item = request.POST.get("Item_name")
        #     sn = request.POST.get("Item_SN")
        #     description = request.POST.get("description")
        #     document = Document.objects.create(file=file, title=name_item)
            
        #     edit_item.name_item=name_item,
        #     edit_item.icon=document,
        #     edit_item.sn=sn,
        #     edit_item.description=description,
            
        #     edit_item.save()
        #     return redirect("/login") 
        # else:
        #     return render(request, "add_item.html", {"form": form})
    
