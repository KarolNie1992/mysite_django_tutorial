"""
Url for creditapp app
"""

from django.urls import path
from . import views

app_name = 'creditapp'

urlpatterns = [
    # ex: /creditapp/
    path('', views.CreditCreateView.as_view(), name='CreditCreateView'),
    # ex: /creditapp/5/results/
    #path('<int:pk>/results/', views.ResultsView.as_view() , name='results'),
    # ex: /creditapp/5/calc/
    path('<int:credit_id>/calc/', views.calc, name='calc'),
]
