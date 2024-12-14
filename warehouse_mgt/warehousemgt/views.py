from django.shortcuts import render,HttpResponse,redirect
from warehousemgt.models import *
from .forms import MyForm
from django.http import JsonResponse
from .models import *
import json








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


def get_item_data(request):
    item_id = request.GET.get('id')  # الحصول على `id` من الطلب
    if not item_id:
        return JsonResponse({'error': 'Item ID not provided'}, status=400)

    try:
        item = Item.objects.get(id=item_id)  # الحصول على العنصر من قاعدة البيانات
        data = {
            'id': item.id,
            'name_item': item.name_item,
            'item_sn': item.sn,
            'description': item.description,
            'isAvailble': item.isAvailble,
            'sold_date': item.sold_date,
            # 'item': item.icon,
            
        }
        print(item.icon.file.url)
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


    
    
def update_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')
        item_name = data.get('name_item')
        item_sn = data.get('item_sn')
        item_description = data.get('description')

        try:
            item = Item.objects.get(id=item_id)
            item.name_item = item_name
            item.sn = item_sn
            item.description = item_description
            item.save()
            return JsonResponse({'success': True})
        except Item.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)