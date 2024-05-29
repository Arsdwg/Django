from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.AuthLogin.as_view(), name='login'),
    path('logout/', views.AuthLogout.as_view(), name='logout'),
    path('user_list/', views.UserList.as_view(), name='list')
]