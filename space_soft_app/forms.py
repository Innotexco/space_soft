from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length=110)
    email = forms.EmailField()
    contact = forms.CharField(max_length = 110)
    address = forms.CharField(max_length = 110)
    message = forms.CharField(widget=forms.Textarea)

class CourseForm(forms.Form):
    name = forms.CharField(max_length=110)
    email = forms.EmailField()
    contact = forms.CharField(max_length = 110)
    address = forms.CharField(max_length = 110)
    course = forms.ChoiceField(choices=[
        ('web', 'Web Development'),
        ('design', 'UI/UX Design'),
        ('android_dev', 'Android Development'),
        ('IOS_dev', 'IOS Development'),
        ('solar', 'Solar Installation'),
        ('electronics', 'Electronics'),
    ])
    message = forms.CharField(widget=forms.Textarea)

