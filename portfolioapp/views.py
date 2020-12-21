from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import WorkModel

# Create your views here.

class WorkList(ListView):
  template_name = 'list.html'
  model = WorkModel

class WorkDetail(DetailView):
  template_name = 'detail.html'
  model = WorkModel

def introduce(request):
  return render(request, 'intro.html', {})