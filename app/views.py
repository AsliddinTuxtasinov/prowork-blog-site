from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import *


class HomePageView(TemplateView):
    template_name = "home.html"

class DetailPageView(TemplateView):
    template_name = "post-detal.html"