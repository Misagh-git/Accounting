from operator import invert
from django.shortcuts import render
from . models import Inventory

# Create your views here.

def display(request):
    Inventorys=Inventory.objects.all().order_by('inventory_name')
    return render(request,"inventory/display_inventory.html",{'Inventorys':Inventorys})
