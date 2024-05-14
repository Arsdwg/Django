from django.shortcuts import render
from . import models

def show_all(request):
    if request.method == 'GET':
        clothes = models.Cloth.objects.filter().order_by('-id')
        return render(request, template_name='cloth/all_cloth.html',
                      context={'clothes': clothes})


def show_male(request):
    if request.method == 'GET':
        male = models.Cloth.objects.filter(tags__name='мужское').order_by('-id')
        return render(request, template_name='cloth/male_cloth.html',
                      context={'male': male})

def show_female(request):
    if request.method == 'GET':
        female = models.Cloth.objects.filter(tags__name='женское').order_by('-id')
        return render(request, template_name='cloth/female_cloth.html',
                      context={'female': female})

def show_kids(request):
    if request.method == 'GET':
        kids = models.Cloth.objects.filter(tags__name='детское').order_by('-id')
        return render(request, template_name='cloth/kid_cloth.html',
                      context={'kids': kids})