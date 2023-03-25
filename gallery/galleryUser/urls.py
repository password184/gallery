from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user-account/', views.userAccount, name="user-account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    
]