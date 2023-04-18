from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView
app_name = "product"


#  views

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from django import views
def ProductView(request):
    product= Product.objects.all()
    var= Variant.objects.all()
   
    price= ProductVariantPrice.objects.all()
    paginator=Paginator(product,2)
    page_number=request.GET.get('page')
    productfinal=paginator.get_page(page_number)

    if request.method=="GET":
        search=request.GET.get('title')
        if search!=None:
            productfinal=Product.objects.filter(title__icontains=search)
    # if request.method=="GET":
    #     variant=request.GET.get('variant')
    #     if variant!=None:
    #         productfinal=Product.objects.filter(title=variant)
    # if request.method=="GET":
    #     min=request.GET.get('price_from')
    #     max=request.GET.get('price_to')
    #     if variant!=None:
    #         productfinal=Product.objects.filter(price__range=(min, max))

    # if request.method=="GET":
    #     date=request.GET.get('date')
    #     if date!=None:
    #         productfinal=Product.objects.filter(created_at=date)



    
    context={
        'product':productfinal,
        'productlength':product,
        'var':var,
        'price':price
    }
    return render(request,'products/list.html',context)
#  end views


urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list2/', TemplateView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),
    path('list/',ProductView,name='list')
    
]
