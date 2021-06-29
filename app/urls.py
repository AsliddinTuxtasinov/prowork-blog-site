from django.urls import path

from .views import HomePageView, DetailPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="index"),
    path('post', DetailPageView.as_view(), name="post"),
    path('hashtag', DetailPageView.as_view(), name="hashtag"),
]
