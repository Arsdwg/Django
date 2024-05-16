from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models, forms
from .models import PostBook

# Create your views here.

def post_not_full(request):
    if request.method == 'GET':
        posts = PostBook.objects.filter().order_by('-id')
        return render(request, template_name='post.html',
                      context={'posts': posts})

def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Ты зарегал новую книгу!</h1>\n'
                                '<a href="/books/" >Домой</a>')
    else:
        form = forms.BookForm()
    return render(request, template_name='create_book.html',
                  context={'form': form})

def redact_book_view(request, id):
    book_id = get_object_or_404(models.PostBook, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Ты исправил книгу!</h1>\n'
                                '<a href="/books/" >Домой</a>')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='edit_book.html',
                  context={'book_id': book_id,
                           'form': form})


def delete_book_view(request, id):
    book_id = get_object_or_404(models.PostBook, id=id)
    book_id.delete()
    return HttpResponse('Book deleted')


def create_review_view(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Ты зарегал новый отзыв!</h1>\n'
                                '<a href="/books/" >Домой</a>')
    else:
        form = forms.ReviewForm()
    return render(request, template_name='create_review.html',
                  context={'form': form})


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
