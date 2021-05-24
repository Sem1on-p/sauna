from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.
def proposal(request):
	return render(request, 'proposal/index.html')