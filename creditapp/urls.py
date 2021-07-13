"""
Url for creditapp app
"""

from django.urls import path
from . import views

app_name = 'creditapp'

urlpatterns = [
    # ex: /creditapp/
    path('', views.Credit_new, name='Credit_new'),
    # ex: /creditapp/5/results/
    ##path('<int:pk>/results/', views.ResultsView , name='ResultsView'),
    # ex: /creditapp/5/calc/
    #path('<int:credit_id>/calc/', views.calc, name='calc'),
]
