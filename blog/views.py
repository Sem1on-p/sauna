from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from . import models

# Create your views here.
def blog_list(request):
	a = models.Article.objects.all()
	return render(request, 'blog/list.html', {'list':a})