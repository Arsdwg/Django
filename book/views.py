from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from django.views import generic
from . import models, forms
from .models import PostBook

# Create your views here.

# List
class PostNotFull(generic.ListView):
    template_name = 'post.html'
    context_object_name = 'posts'
    model = models.PostBook

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")

# def post_not_full(request):
#     if request.method == 'GET':
#         posts = PostBook.objects.filter().order_by('-id')
#         return render(request, template_name='post.html',
#                       context={'posts': posts})


# Create

class CreateBook(generic.CreateView):
    template_name = 'create_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBook, self).form_valid(form=form)


# def create_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Ты зарегал новую книгу!</h1>\n'
#                                 '<a href="/books/" >Домой</a>')
#     else:
#         form = forms.BookForm()
#     return render(request, template_name='create_book.html',
#                   context={'form': form})


# Redact

class UpdateBook(generic.UpdateView):
    template_name = 'edit_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.PostBook, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBook, self).form_valid(form=form)



# def redact_book_view(request, id):
#     book_id = get_object_or_404(models.PostBook, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Ты исправил книгу!</h1>\n'
#                                 '<a href="/books/" >Домой</a>')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, template_name='edit_book.html',
#                   context={'book_id': book_id,
#                            'form': form})


# Delete
class DeleteBook(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/books/'

    def get_object(self, queryset=None):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.PostBook, id=book_id)

# def delete_book_view(request, id):
#     book_id = get_object_or_404(models.PostBook, id=id)
#     book_id.delete()
#     return HttpResponse('Book deleted')

# CreateReview

class CreateReviewBook(generic.CreateView):
    template_name = 'create_review.html'
    form_class = forms.ReviewForm
    success_url = '/books/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewBook, self).form_valid(form=form)

#
# def create_review_view(request):
#     if request.method == 'POST':
#         form = forms.ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Ты зарегал новый отзыв!</h1>\n'
#                                 '<a href="/books/" >Домой</a>')
#     else:
#         form = forms.ReviewForm()
#     return render(request, template_name='create_review.html',
#                   context={'form': form})



# Detail
class PostMore(generic.DetailView):
    template_name = 'post_detail.html'
    context_object_name = 'post_id'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.PostBook, id=post_id)



# def post_more(request, id):
#     if request.method == 'GET':
#         post_id = get_object_or_404(PostBook, id=id)
#         return render(request, template_name='post_detail.html', context={'post_id': post_id})


#
# def hello_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Hurray, its Arseniy Turusbekov!')
#
#
# def hobby_view(request):
#     if request.method == 'GET':
#         return HttpResponse('I love travelling.')
#
#
# def time_view(request):
#     if request.method == 'GET':
#         return HttpResponse(f'{datetime.datetime.now()}')
