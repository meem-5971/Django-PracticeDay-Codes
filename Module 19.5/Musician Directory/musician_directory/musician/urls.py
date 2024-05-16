from django.urls import path,include
from . import views
urlpatterns = [
    path('add_musician/' , views.AddMusicianView.as_view() , name='add_musician'),
    path('edit_musician/<int:id>',views.EditMusicianView.as_view(),name='edit_musician'),
]