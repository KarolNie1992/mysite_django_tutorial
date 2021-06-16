from django.shortcuts import render

# Create your views here.

def Portfolio_index(request):
    return render(request, 'portfolio/index.html',{})