from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hurray, its Arseniy Turusbekov!')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('I love travelling.')


def time_view(request):
    if request.method == 'GET':
        return HttpResponse(f'{datetime.datetime.now()}')