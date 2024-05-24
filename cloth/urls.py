from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowAll.as_view(), name='all_cloth'),
    path('male_cloth/', views.ShowMale.as_view(), name='male_cloth'),
    path('female_cloth/', views.ShowFemale.as_view(), name='female_cloth'),
    path('kid_cloth/', views.ShowKids.as_view(), name='kid_cloth')
]
