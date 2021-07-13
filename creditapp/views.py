"""
Views for credit app
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import loader
from django.views import generic

from .models import Credit
from .forms import CreditCreateForm

def Credit_new(request):
    if request.method == 'POST':
        form = CreditCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            try:
                q = 1 + ((post.interest_rate/100)/12)
                vInstallment = round(post.creditValue * (pow(q,post.installmentsVal)) * ((q-1)/(pow(q,post.installmentsVal)-1)), 2)
                post.totalAmountRepaid = vInstallment * post.installmentsVal
                post.monthlyInstallment = vInstallment
                post.creditResultDate = timezone.now()

                # Czy użytkownika stać na kredyt?, 
                # Kwota jaka pozostanie po obliczeniu 
                # różnicy pomiędzy przychodem a wydatkami                
                maxMonthlyInstallment = post.monthlyIncome - post.monthlyExpenses

                if post.monthlyInstallment > maxMonthlyInstallment:
                    return render(request, 'creditapp/credit_create_form.html', {
                        'form': form,
                        'error_message': "Error!, You cannot get a loan, the loan installment exceeds your creditworthiness",
                    })
                else:    
                    post.save()
            except ZeroDivisionError:
                return render(request, 'creditapp/credit_create_form.html', {
                    'form': form,
                    'error_message': "Error!, You can't divide by zero!",
                })
            else:
                #return redirect('creditapp:ResultsView',pk=post.pk)
                return render (request, 'creditapp/credit_create_form.html',{
                    'form': form,
                    'totalAmountRepaid': post.totalAmountRepaid,
                    'monthlyInstallment': post.monthlyInstallment,
                    'calc': True,
                })
    else:
        form = CreditCreateForm()
    return render(request, 'creditapp/credit_create_form.html',
                  {'form': form})

#def ResultsView(request, pk):
#    post = get_object_or_404(Credit, pk=pk)    
#    return render(request, 'creditapp/results.html', {'form': post,})
    
