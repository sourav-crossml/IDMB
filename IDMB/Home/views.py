from django.http import request
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.urls import reverse


def index(request):
    """
    this function will help in adding movie
    """
    form=MovieForm
    if request.method=='POST':
	    add_movie=MovieForm(request.POST)
	    if add_movie.is_valid():
		    add_movie.save()
		    return render(request,'Home/index.html',{'form':form})
    return render(request,'Home/index.html',{'form':form})


def artist(request):
    """
    this function will help in add artist
    """
    form=ArtistForm
    if request.method=='POST':
	    add_movie=ArtistForm(request.POST)
	    if add_movie.is_valid():
		    add_movie.save()
		    return render(request,'Home/index.html',{'form':form})
    return render(request,'Home/index.html',{'form':form})


def award(request):
    """
    this function will help in add award
    """
    form=AwardForm
    if request.method=='POST':
	    add_movie=AwardForm(request.POST)
	    if add_movie.is_valid():
		    add_movie.save()
		    return render(request,'Home/index.html',{'form':form})
    return render(request,'Home/index.html',{'form':form})


def rating(request):
        """
        this function will help in add and getting average of rating
        """
        if request.method == "POST":
            rate_form = RatingForm(request.POST)
        # print(type(rate_form))
            if rate_form.is_valid():
                form_object =  rate_form.save(commit=False)
                form_object.movie = rate_form.cleaned_data.get('movie')
                form_object.movie_rating = rate_form.cleaned_data['movie_rating']
                filtered_data = Rating.objects.filter(
                    movie=form_object.movie, movie_rating=form_object.movie_rating)
                if filtered_data.count() >= 1:
                    rate_obj = filtered_data.get()
                    rate_obj.votes += 1
                    rate_obj.save()
                else:
                    form_object.votes = 1
                    form_object.save()
                    form_object.movie.save()
                movie = Movies.objects.get(name=form_object.movie)
                rating_obj = Rating.objects.filter(movie=movie)
                rating_list = [int(rating_data.votes)*int(rating_data.movie_rating) for rating_data in rating_obj]
                vote_list = [rating_data.votes for rating_data in rating_obj]
                movie.avg_rating = sum(rating_list)/sum(vote_list)
                movie.save()
                messages.success(request, "Rated Successfully !")
                return redirect(reverse('Home:rating'))
            else:
                messages.error(request, "Error While Rating ")
                return redirect(reverse('Home:rating'))
        else:
            rate_form = RatingForm()
            context = {'form':rate_form}
            return render(request, 'Home/index.html', context)


def topten(request):
    """
    this function will help in getting top ten movies by average  
    """
    movies= Movies.objects.all().order_by('-avg_rating')[:5]
    return render(request, 'Home/display.html', {"context": movies})


def leastten(request):
    """
    this function will help in getting last ten movies by average
    """
    movies= Movies.objects.all().order_by('avg_rating')[:5]
    return render(request, 'Home/display.html', {"context": movies})

def within(request):   
    """
    this function will help in getting movies within a date span
    """
    if request.POST:
        breakpoint()
        start_date = request.POST['startdate']
        end_date = request.POST['enddate']
        print(start_date,end_date)
        movies = Movies.objects.filter(release_date__range=[start_date, end_date])
        return render(request, 'Home/display.html', {"context": movies, "title": f'Search from {start_date} to {end_date}'})

def search_results(request):
    """
    this function will help to search movies by artist name and movie name
    """
    form = SearchForm(request.POST or None)
    queryset = None
    if request.method == 'POST':
        queryset = Movies.objects.filter(name__icontains=form['name'].value()) or Movies.objects.filter(artists__artist=form['name'].value())
        print(queryset)
    context = {
        "form": form,
        "queryset": queryset}
    return render(request, 'Home/details.html', context)