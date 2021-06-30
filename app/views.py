from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from app.models import Blog, Category, Regions, Hashtags, PicturesFromTheBlog

# home page view
class HomePageView(ListView):
    template_name = 'home.html'
    queryset = Blog.objects.all()
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions'] = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        # context['blogs'] = Blog.objects.all()
        return context


class SinglePageView(DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'post-detal.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions'] = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context


class CatagoryPageView(ListView):
    template_name = 'home.html'
    model = Blog
    context_object_name = 'post'

    def get_queryset(self):
        queryset = self.model.objects.filter(category__slug=self.kwargs.get('slug'))
        return queryset

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions'] = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context


class RegionsPageView(ListView):
    template_name = 'home.html'
    model = Blog
    context_object_name = 'post'

    def get_queryset(self):
        queryset = self.model.objects.filter(region__slug=self.kwargs.get('slug'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions'] = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context


class HashtegsPageView(ListView):
    template_name = 'home.html'
    model = Blog
    context_object_name = 'post'

    def get_queryset(self):
        queryset = self.model.objects.filter(hashtag__slug=self.kwargs.get('slug'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions'] = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context