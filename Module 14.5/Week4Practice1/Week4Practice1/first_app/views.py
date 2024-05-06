from django.shortcuts import render
from first_app.forms import StudentForm
from first_app.models import StudentModel

# Create your views here.
def home(request):   
    return render(request, 'base.html')

def modelview(request):
    data= StudentModel.objects.all()
    return render(request, 'model.html' , {'data' : data})


def formview(request):
    if request.method == 'POST':
        form = StudentForm(request.POST , request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        
        form = StudentForm()
    return render(request, 'form.html' , {'form' : form})  
