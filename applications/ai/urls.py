from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = 'ai'
urlpatterns = [
    path('', views.GPTCode, name='gpt_code'),
]
