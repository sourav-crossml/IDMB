from django.forms import ModelForm, widgets
from django import forms
from . models import *
class DateInput(forms.DateInput):
    input_type='date'


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        widgets={
            'release_date':DateInput(),
        }
        exclude = ['avg_rating']

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets={
            'dob':DateInput(),
        }

class AwardForm(ModelForm):
    class Meta:
        model = Awards
        fields = '__all__'
        widgets={
            'date':DateInput(),
        }


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
        exclude = ['votes']


class SearchForm(ModelForm):
   class Meta:
     model = Movies
     fields = [ 'name']