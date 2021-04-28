"""
Url for creditapp app
"""

from django.urls import path
from . import views

app_name = 'creditapp'

urlpatterns = [
    # ex: /creditapp/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /creditapp/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view() , name='results'),
]
