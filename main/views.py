from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.
def main_page(request):
	return render(request, 'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def calc(request):
	return render(request, 'main/calc.html')

def contact(request):
	return render(request, 'main/contacts.html')