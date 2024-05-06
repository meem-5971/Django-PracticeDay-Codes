from django import forms
from first_app.models import StudentModel
import datetime

yrs = ['2020','2021','2022','2023']
seasons = [('SUMMER','summer'),("WINTER","winter"),("SPRING","spring")]

class StudentForm(forms.Form):
    name = forms.CharField(label='Student Name',  widget=forms.Textarea(attrs={'rows':2}))
    email = forms.EmailField(help_text='Enter your email address')
    HSC_Completed = forms.BooleanField()
    passing_year = forms.DateField(widget=forms.SelectDateWidget(years=yrs))
    HSC_registration_number = forms.DecimalField()
    apply_date = forms.DateField(initial=datetime.date.today())
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fav_season = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=seasons)
    passport_image = forms.ImageField()
    cv=forms.FileField
    