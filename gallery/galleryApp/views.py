from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gallery
from .forms import GalleryForm
from django.db.models import Q
from django.core.paginator import Paginator

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def gallery(request):
    search = ''
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        print('Search:', search )

    gallery = Gallery.objects.filter(Q(name__icontains=search) | Q(category__icontains=search))
    context = {'gallerys': gallery, 'search': search}
    return render(request, "gallery.html", context)

def createGallery(request):
    about = request.user.about
    form = GalleryForm()

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.owner = about
            gallery.save()
            return redirect('gallery')

    context = {'form': form}
    return render(request, "gallery_form.html", context)





def editGallery(request, pk):
    about = request.user.about
    gallery = about.gallery_set.get(id=pk)
    form = GalleryForm(instance=gallery)

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('user-account')

    context = {'form': form}
    return render(request, "gallery_form.html", context)

def deleteGallery(request, pk):
    about = request.user.about
    gallery = about.gallery_set.get(id=pk)

    if request.method == 'POST':
        gallery.delete()
        return redirect('gallery')

    context = {'gallery': gallery}
    return render(request, "delete_form.html", context)

