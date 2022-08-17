from django.shortcuts import render
from .models import Iphone

# Create your views here.

def index(request):
    return render(request, 'base.html')

def iphonePM(request):
    iphones=Iphone.objects.all()
    context={'iphones':iphones}
    
    return render(request, 'iphone.html',context)
