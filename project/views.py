from django.shortcuts import render, reverse
from . import models
from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.
def project(request):
	projects = models.Project.objects.all()
	return render(request, 'project/index.html', {'projects': projects})

