from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Musician
from .forms import MusicianForm
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return Musician.objects.get(pk=id)
