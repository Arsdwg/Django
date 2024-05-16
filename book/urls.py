from django.urls import path
from  . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('hobby/', views.hobby_view, name='hobby'),
    path('time/', views.time_view, name='time'),
    path('books/', views.post_not_full, name='books'),
    path('books/<int:id>/', views.post_more, name='detail'),
    path('books/<int:id>/delete/', views.delete_book_view, name='delete'),
    path('books/<int:id>/update/', views.redact_book_view, name='update'),
    path('create/', views.create_book_view, name='create'),
    path('create_review/', views.create_review_view, name='create_review')
]