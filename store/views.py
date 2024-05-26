from django.shortcuts import render, HttpResponse
from django.views import generic
from . import models


def storehome(request):
    products = models.Product.objects.all()
    context = {'products' : products}
    return render(request, "store/home.html", context)
    
def good_details(request, pk):
    product = models.Product.objects.get(id=pk)
    context = {'product' : product}
    return render(request, "store/good_details.html", context)

def about(request):
    return HttpResponse("About this site")

