"""
Views for credit app
"""
from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from django.views import generic

from .models import Credit, CreditResult

class CreditCreateView(generic.CreateView):
    """
    Index for credit app, Main window
    """
    template_name = 'creditapp/credit_create_form.html'
    model = Credit
    fields = ['credit_name_text',
                'interest_rate',
                'installmentsVal',
                'creditValue',
                'monthlyIncome',
                'monthlyExpenses']

#class CreditResultsView(generic.DetailView):


def calc(request, credit_id):
    """
    Calculation of credit
    """


