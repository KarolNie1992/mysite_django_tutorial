"""
Url for viewOnSnow app
"""

from django.urls import path
from . import views

app_name = 'viewonsnow'

urlpatterns = [
    # ex: /
    path('', views.viewonsnow_index, name='viewonsnow_index'),
]
