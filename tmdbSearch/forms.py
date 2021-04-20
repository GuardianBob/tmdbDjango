from .models import Movie
from django import forms
import datetime

class searchForm(forms.Form):
    title = forms.CharField(max_length = 200)
    