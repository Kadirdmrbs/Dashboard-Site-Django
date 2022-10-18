from django.shortcuts import render
from decouple import config

# Create your views here.

def ml_view(request):

    my_var = {'num':31,
    'name':config('SECRET_KEY'),
    'text':config('SECRET_TEXT')}

    return render(request,'prediction/ml.html',context=my_var)