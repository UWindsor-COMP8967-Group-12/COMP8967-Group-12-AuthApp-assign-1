from django.shortcuts import render, redirect

from .forms import EditPhoto
from .models import Category, Photo
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def photos(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/photos.html', context)


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

        return redirect('photos')

    context = {'categories': categories}
    return render(request, 'photos/addPhoto.html', context)


# need to enter password again to delete photo
@login_required(login_url='login')
def deletePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('photos')

    context = {'photo': photo}
    return render(request, 'photos/deletePhoto.html', context)


@login_required(login_url='login')
def updatePhoto(request, pk):
    if request.method == 'POST':
        photo = Photo.objects.get(id=pk)
        form = EditPhoto(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photos')
    else:
        photo = Photo.objects.get(id=pk)
        form = EditPhoto(instance=photo)

    context = {'form': form}
    return render(request, 'photos/updatePhoto.html', context)
