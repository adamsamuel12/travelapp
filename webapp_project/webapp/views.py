from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import App
from .forms import App_Form


# Create your views here.
def index(request):
    movie = App.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def details(request, id):
    movie = App.objects.get(id=id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        app = App(name=name, description=description, year=year, image=image)
        app.save()
    return render(request, 'add.html')


def update(request, id):
    movie = App.objects.get(id=id)
    form = App_Form(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = App.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
