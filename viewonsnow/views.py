from django.http.response import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response

from .functions import viewOnSnow

from .models import Snow
from .forms import SnowCreateForm

User = get_user_model()

# Create your views here.

def viewonsnow_index(request):
    if request.method == 'POST':
        form = SnowCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            try:
                #pobieramy wprowadzone dane i przerabiamy na listę
                inputString = post.input_before_snow
                inputList = [int(s) for s in inputString.split(',')]

                #funkcja oczekuje listy, wartość początkowa przed opadami śniegu
                #funkcja zwraca stan po opadach śniegu 
                outputList = viewOnSnow(inputList)
                post.output_after_snow = ','.join([str(elem) for elem in outputList])
                post.save()


            except NotImplementedError:
                return render(request, 'viewonsnow/main.html', {
                    'form': form,
                    'error_message': "Error!",
                })
            
            else:
                form_data = form.cleaned_data
                return render (request, 'viewonsnow/main.html',{
                    'form': form_data,
                    'output_after_snow': post.output_after_snow,
                    'calc': True,
                    'calc_id': post.id,
                })

        else:
            return render(request, 'viewonsnow/main.html',
            {
                'form': form,
                'error_message': form.errors.values(),
            })     

    else:
        form = SnowCreateForm()
    return render(request, 'viewonsnow/main.html',
                  {'form': form})

def get_data(request, calc_id, **kwargs):
    
    calc = get_object_or_404(Snow, pk = calc_id)
    #konwersja stringu z DB do listy
    outputList = [int(s) for s in calc.output_after_snow.split(',')]
    inputList = [int(s) for s in calc.input_before_snow.split(',')]

    #utworzenie listy dla labels
    size = len(outputList)
    labels = list(range(1, size + 1))

    data = {
        "id": calc_id,
        "labels": labels,
        "output_after_snow": outputList,
        "input_before_snow": inputList,
    }

    return JsonResponse(data) #http response



class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['Users', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [qs_count, 2, 3, 4, 5, 6]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)

    