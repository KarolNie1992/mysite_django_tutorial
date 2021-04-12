"""
Views for polls app
"""
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question #, Choice

# Create your views here.

def index(request):
    """
    Index for polls app
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return render(request,'polls/index.html', context)

def detail(request, question_id):
    """
    Details for polls app
    https://docs.djangoproject.com/pl/3.2/intro/tutorial03/#a-shortcut-get-object-or-404
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist as question_doesnotexist:
        raise Http404 ("Question does not exist.") from question_doesnotexist
    return render(request,'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    Results for polls app
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """
    Vote for polls app
    """
    return HttpResponse("You're voting on question %s." % question_id)
