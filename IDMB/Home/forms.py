from django.forms import ModelForm, widgets
from django import forms
from . models import *
class DateInput(forms.DateInput):
    """
    this class will get callender for date field
    """
    input_type='date'


class MovieForm(ModelForm):
    """
    this model will work for saving data from UI to movie model
    """
    class Meta:
        model = Movies
        fields = '__all__'
        widgets={
            'release_date':DateInput(),
        }
        exclude = ['avg_rating']

class ArtistForm(ModelForm):
    """
    this model will work for saving data from UI to artist model
    """
    class Meta:
        model = Artist
        fields = '__all__'
        widgets={
            'dob':DateInput(),
        }

class AwardForm(ModelForm):
    """
    this model will work for saving data from UI to award model
    """
    class Meta:
        model = Awards
        fields = '__all__'
        widgets={
            'date':DateInput(),
        }


class RatingForm(ModelForm):
    """
    this model will work for saving data from UI to rating model
    """
    class Meta:
        model = Rating
        fields = '__all__'
        exclude = ['votes']


class SearchForm(ModelForm):
    """
    this model will help in searching data from movie model
    """
    class Meta:
        model = Movies
        fields = [ 'name']