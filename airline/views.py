
from django.shortcuts import render


def home(request):
    return render(request, 'airline/home.html', context={
        'name': 'fabiana',
    }) 
