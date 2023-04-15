from django.shortcuts import render
from .models import *

# Create your views here.
from django import views

def ProductView(request):
    pd= Product.objects.all()
    

    context={
        'pd':pd,
    }
    return render(request,'products/list.html',context)