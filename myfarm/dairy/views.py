from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def current_time(request):
    current_date_time = datetime.datetime.now()
    return HttpResponse(f"The Current time: {current_date_time}")
