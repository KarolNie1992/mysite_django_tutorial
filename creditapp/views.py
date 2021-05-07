"""
Views for credit app
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import loader
from django.views import generic

from .models import Credit, CreditResult
from .forms import CreditCreateForm

def Credit_new(request):
    if request.method == 'POST':
        form = CreditCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            
            post.save()
            return redirect('creditapp:ResultsView',pk=post.pk)
    else:
        form = CreditCreateForm()
    return render(request, 'creditapp/credit_create_form.html',
                    {'form': form})

def ResultsView(request, pk):
    post = get_object_or_404(Credit, pk=pk)
    try:
        q = 1 + ((post.interest_rate/100)/12)
        vInstallment = round(post.creditValue * (pow(q,post.installmentsVal)) * ((q-1)/(pow(q,post.installmentsVal)-1)), 2)
        
        vtotalAmountRepaid = vInstallment * post.installmentsVal
        creditresult = post.creditresult_set.create(monthlyInstallment=vInstallment,
                                                    totalAmountRepaid=vtotalAmountRepaid,
                                                    creditResultDate=timezone.now())
        creditresult.save()
    except ZeroDivisionError:
        return render(request, 'creditapp/credit_create_form.html', {
            'form': post,
            'error_message': "Error!, You can't divide by zero!",
        })
    else:        
        return render(request, 'creditapp/results.html', {'form': post, 'res': creditresult,})
    
