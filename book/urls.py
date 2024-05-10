from django.urls import path
from .views import hello_view, hobby_view, time_view, post_not_full, post_more

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', time_view, name='time'),
    path('books/', post_not_full, name='books'),
    path('books/<int:id>/', post_more, name='detail')
]

