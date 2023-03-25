from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name="gallery"),
    path('create_gallery/', views.createGallery, name="create_gallery"),
    path('edit_gallery/<str:pk>/', views.editGallery, name="edit_gallery"),
    path('delete_gallery/<str:pk>/', views.deleteGallery, name="delete_gallery"),
]