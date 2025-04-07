from django import forms

class student_form(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField
    email=forms.EmailField
    gender=forms.CharField(widget=forms.RadioSelect(choices=[("male","Male"),("female","Female"),("others","Others")]))
    agree=forms.CharField(widget=forms.CheckboxInput())