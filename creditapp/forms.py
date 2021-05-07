from django import forms

from .models import Credit, CreditResult

class CreditCreateForm(forms.ModelForm):
    """
    Index for credit app, Main window
    """
    class Meta:
        model = Credit
        fields = ['credit_name_text',
                'interest_rate',
                'installmentsVal',
                'creditValue',
                'monthlyIncome',
                'monthlyExpenses']