from django.shortcuts import render

# Create your views here.

def ml_view(request):
    return render(request,'prediction/ml.html')