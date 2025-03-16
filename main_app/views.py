# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
   return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')