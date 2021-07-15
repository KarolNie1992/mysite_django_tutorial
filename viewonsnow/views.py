from django.shortcuts import render

from .functions import viewOnSnow

from .models import Snow
from .forms import SnowCreateForm

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
                post.output_after_snow = viewOnSnow(inputList)

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

