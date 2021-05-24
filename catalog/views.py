from django.shortcuts import render, reverse
from . import models
from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.
def catalog(request):
	product_list = models.Product.objects.all()
	ready_categories = models.Category.objects.filter(categories_type='R')
	order_categories = models.Category.objects.filter(categories_type='O')
	return render(request, 'catalog/catalog.html', {'product_list': product_list, 'ready_categories': ready_categories,
													'order_categories': order_categories})

def price(request):
	return render(request, 'catalog/price.html')

