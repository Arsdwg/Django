from django.urls import path
from . import views

urlpatterns = [
    # path('hello/', views.hello_view, name='hello'),
    # path('hobby/', views.hobby_view, name='hobby'),
    # path('time/', views.time_view, name='time'),
    path("books/", views.PostNotFull.as_view(), name="books"),
    path("books/<int:id>/", views.PostMore.as_view(), name="detail"),
    path("books/<int:id>/delete/", views.DeleteBook.as_view(), name="delete"),
    path("books/<int:id>/update/", views.UpdateBook.as_view(), name="update"),
    path("create/", views.CreateBook.as_view(), name="create"),
    path("create_review/", views.CreateReviewBook.as_view(), name="create_review"),
]
