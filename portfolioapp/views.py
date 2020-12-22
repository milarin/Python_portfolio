
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import WorkModel
from .form import ContactForm

# Create your views here.

class WorkList(ListView):
  template_name = 'list.html'
  model = WorkModel

class WorkDetail(DetailView):
  template_name = 'detail.html'
  model = WorkModel

def introduce(request):
  return render(request, 'intro.html', {})

class ContactView(FormView):
  template_name = 'contact.html'
  form_class = ContactForm
  success_url = reverse_lazy('result')

  def form_valid(self, form):
    form.send_email()
    return super().form_valid(form)

class ContactResultView(TemplateView):
  template_name = 'result.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['success'] = "お問い合わせは正常に送信されました。"
    return context