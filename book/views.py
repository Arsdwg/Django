from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from .models import PostBook, Review

# Create your views here.

def post_not_full(request):
    if request.method == 'GET':
        posts = PostBook.objects.filter().order_by('-id')
        return render(request, template_name='post.html',
                      context={'posts': posts})


def post_more(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(PostBook, id=id)
        return render(request, template_name='post_detail.html', context={'post_id': post_id})

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hurray, its Arseniy Turusbekov!')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('I love travelling.')


def time_view(request):
    if request.method == 'GET':
        return HttpResponse(f'{datetime.datetime.now()}')