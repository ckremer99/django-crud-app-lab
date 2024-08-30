from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request): 
    animals = Animal.objects.filter(user=request.user)
    return render(request, 'animals/index.html', {'animals': animals})

def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    feeding_form = FeedingForm()
    return render(request, 'animals/detail.html', {
        'animal': animal,
        'feeding_form': feeding_form,
    })

def add_feeding(request, animal_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.animal_id = animal_id
        new_feeding.save()
    return redirect('animal-detail', animal_id=animal_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('animal-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class AnimalCreate(CreateView): 
    model = Animal
    fields = ['name', 'type', 'description', 'age']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['type', 'description', 'age']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'

class Home(LoginView):
    template_name = 'home.html'