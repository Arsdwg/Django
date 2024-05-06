from django.urls import path
from .views import hello_view, hobby_view, time_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', time_view, name='time')
]

