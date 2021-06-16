"""
Url for portfolio app
"""

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # ex: /
    path('', views.Portfolio_index, name='Portfolio_index'),
]
