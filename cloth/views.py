from django.shortcuts import render
from django.views import generic
from . import models


class ShowAll(generic.ListView):
    template_name = 'cloth/all_cloth.html'
    context_object_name = 'clothes'
    model = models.Cloth


    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

# def show_all(request):
#     if request.method == 'GET':
#         clothes = models.Cloth.objects.filter().order_by('-id')
#         return render(request, template_name='cloth/all_cloth.html',
#                       context={'clothes': clothes})



class ShowMale(generic.ListView):
    template_name = 'cloth/male_cloth.html'
    context_object_name = 'male'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='мужское').order_by('-id')


# def show_male(request):
#     if request.method == 'GET':
#         male = models.Cloth.objects.filter(tags__name='мужское').order_by('-id')
#         return render(request, template_name='cloth/male_cloth.html',
#                       context={'male': male})


class ShowFemale(generic.ListView):
    template_name = 'cloth/female_cloth.html'
    context_object_name = 'female'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='женское').order_by('-id')

# def show_female(request):
#     if request.method == 'GET':
#         female = models.Cloth.objects.filter(tags__name='женское').order_by('-id')
#         return render(request, template_name='cloth/female_cloth.html',
#                       context={'female': female})



class ShowKids(generic.ListView):
    template_name = 'cloth/kid_cloth.html'
    context_object_name = 'kids'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='детское').order_by('-id')


# def show_kids(request):
#     if request.method == 'GET':
#         kids = models.Cloth.objects.filter(tags__name='детское').order_by('-id')
#         return render(request, template_name='cloth/kid_cloth.html',
#                       context={'kids': kids})