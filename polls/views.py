"""
Views for polls app
"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    """
    Index for polls app
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def show_question_with_choices(self):
        return Question.objects.exclude(choice__isnull=True)

    def get_queryset(self):
        """
        Return the last five published questions 
        (not including those set to be published in the future). 
        Not empty questions.
        """
        return self.show_question_with_choices().filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        #return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def show_question_with_choices(self):
        return Question.objects.exclude(choice__isnull=True)

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return self.show_question_with_choices().filter(pub_date__lte=timezone.now())
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def show_question_with_choices(self):
        return Question.objects.exclude(choice__isnull=True)

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet from result window. 
        """
        return self.show_question_with_choices().filter(pub_date__lte=timezone.now())
    


#def detail(request, question_id):
    """
    Details for polls app
    https://docs.djangoproject.com/pl/3.2/intro/tutorial03/#a-shortcut-get-object-or-404
    """
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist as question_doesnotexist:
        raise Http404 ("Question does not exist.") from question_doesnotexist
    return render(request,'polls/detail.html', {'question': question})
    """
 #   question = get_object_or_404(Question, pk=question_id)
 #   return render(request,'polls/detail.html', {
 #       'question': question,
 #       })
# def results(request, question_id):
#     """
#     Results for polls app
#     """
#     question = get_object_or_404( Question, pk=question_id )
#     return render(request, 'polls/results.html', {'question': question,})

def vote(request, question_id):
    """
    Vote for polls app
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
