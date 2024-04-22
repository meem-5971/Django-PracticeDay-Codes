from django.shortcuts import render
from datetime import date,datetime

def index(request):
    return render(request,'sample_app/index.html')

def filter(request):
    data ={
        'name':"khushnor rahman meem",
        'id' : "5971",
        'gender':"female",
        'department':"cs'e",
        'DOB':date(2000, 5, 1),
        'drama':['k2','mighty','flower','midnight'],
        'empty':"",
        'val':[
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],
        'li':{'a','b','c','d','e'},
        'date':datetime.now()
    }
    return render(request,'sample_app/filter.html',data)
