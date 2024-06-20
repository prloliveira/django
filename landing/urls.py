from django.urls import path
from landing.views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    # Add more URL patterns here
]