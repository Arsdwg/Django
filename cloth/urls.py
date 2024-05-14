from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all, name='all_cloth'),
    path('male_cloth/', views.show_male, name='male_cloth'),
    path('female_cloth/', views.show_female, name='female_cloth'),
    path('kid_cloth/', views.show_kids, name='kid_cloth')
]
