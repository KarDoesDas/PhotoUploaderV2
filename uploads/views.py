from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.

@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)



def deletePhoto(request, pk):
    user = request.user
    photo = Photo.objects.get(id=pk)
    if request.method == "POST":
        photo.delete()
        return redirect('gallery')
    context = {'photo': photo}
    return render(request, 'photos/delete.html', context)


def deleteFolder(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if request.method == "POST":
        category.delete()
        return redirect('gallery')
    context = {'category': category}
    return render(request, 'photos/deleteFolder.html', context)

