from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from app.models import Blog, Category, Regions, Hashtags, PicturesFromTheBlog

# home page view
class HomePageView(ListView):
    template_name = 'home.html'
    queryset = Blog.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions'] = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        # context['blogs'] = Blog.objects.all()
        return context



class DetailPageView(TemplateView):
    template_name = "post-detal.html"