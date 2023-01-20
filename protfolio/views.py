from django.shortcuts import render

# Create your views here.

from .models import *

# Create your views here.
def protfolio(request):
     

     info = Informations.objects.get(name = "abdelghny")
     projects = Projects.objects.all()
     context = {'info': info, 'projects':projects}


     return render(request, 'protfolio/about.html', context)

# def home(request):

#     return render(request, 'portfolio/home.html')