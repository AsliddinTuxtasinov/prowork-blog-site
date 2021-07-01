from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from app.models import Blog, Category, Regions, Hashtags, PicturesFromTheBlog

# home page view
class HomePageView(ListView):
    template_name = 'home.html'
    queryset = Blog.objects.all()
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions']  = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context

# Single blog page view
class SinglePageView(DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'post-detal.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions']  = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context

# Filter Catagory page view
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
        context['regions']  = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context

# Filter Regions page view
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
        context['regions']  = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context

# Filter Hashtegs page view
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
        context['regions']  = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context


# Search page Class Based View
class SearchPageView(ListView):
    template_name = 'home.html'
    model = Blog
    context_object_name = 'post'

    def get_queryset(self):
        search = self.request.GET.get('q')
        if search:
            queryset=self.model.objects.filter(
                Q(category__name=search) | Q(hashtag__name=search)
            )
        else:
            queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['regions']  = Regions.objects.all()
        context['hashtegs'] = Hashtags.objects.all()
        return context


# Search page function view
# def searchView(request):
#
#     category = Category.objects.all()
#     regions = Regions.objects.all()
#     hashtegs = Hashtags.objects.all()
#
#     search_post = request.GET.get('search')
#     if search_post:
#         post = Blog.objects.filter(
#             Q(category__name=search_post) | Q(hashtag__name=search_post) #| Q(region__name=search_post)
#         )
#     else:
#         post = Blog.objects.all()
#
#     return render(request,'home.html',{
#         'post':post,
#         'category':category,
#         'regions':regions,
#         'hashtegs':hashtegs
#     })