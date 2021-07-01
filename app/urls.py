from django.urls import path

from app.views import (
    HomePageView, SinglePageView, CatagoryPageView,
    RegionsPageView, HashtegsPageView, SearchPageView #,searchView
)

urlpatterns = [
    path('', HomePageView.as_view(), name = "index" ),
    path( 'post/<slug:slug>', SinglePageView.as_view(), name = "post" ),
    path( 'categories/<slug:slug>', CatagoryPageView.as_view(), name = "categories" ),
    path( 'regions/<slug:slug>', RegionsPageView.as_view(), name = "regions" ),
    path( 'hashtag/<slug:slug>', HashtegsPageView.as_view(), name = "hashtag" ),
    # path( 'search/', searchView, name = "search_post" ), # this is function view
    path( 'search/', SearchPageView.as_view(), name = "search_post" ),
]
