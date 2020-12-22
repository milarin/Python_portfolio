from os import name
from django.contrib import admin
from django.urls import path
from .views import ContactResultView, WorkList, WorkDetail, introduce, ContactView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('list/', WorkList.as_view(), name='list'),
  path('detail/<int:pk>/', WorkDetail.as_view(), name='detail'),
  path('intro/', introduce, name='intro'),
  path('contact/', ContactView.as_view(), name='contact'),
  path('result/', ContactResultView.as_view(), name='result')
]