from django.shortcuts import render,redirect,get_object_or_404
from .models import Album
from .forms import AlbumForm
from django.views.generic import UpdateView,DeleteView,View
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class AddAlbumView(View):
    template_name = 'add_album.html'
    
    def get(self, request, *args, **kwargs):
        album_form = AlbumForm()
        return render(request, self.template_name, {'form': album_form})
    
    def post(self, request, *args, **kwargs):
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
        return render(request, self.template_name, {'form': album_form})
    
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return Album.objects.get(pk=id)
    
class DeleteAlbumView(View):
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        album = get_object_or_404(Album, pk=id)
        album.delete()
        return redirect(self.success_url)