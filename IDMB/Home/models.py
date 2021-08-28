"""
home app will handle all the data of IDMB in this model file
"""
from datetime import datetime
from django.db import models
"""
choices for ratings
"""
CATEGORY_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]
# Create your models here.

class Artist(models.Model):
    """
    this class will manage Artist details and operation on the data related to Artist
    """
    name = models.CharField(max_length=30)
    dob = models.DateField(verbose_name='Date of birth',default=datetime.now)
    gender = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    # Awards_received = models.ForeignKey(Awards, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name

class Awards(models.Model):
    """
    this class will manage Awards details and operation on the data related to Awards
    """
    name = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name



class Movies(models.Model):
    """
    this class will manage movies details and operation on the data related to movies 
    """
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    language = models.CharField(max_length=100)
    artist = models.ManyToManyField(Artist,blank=True)
    length = models.DecimalField(max_digits=3, decimal_places=2)
    awards_received = models.ManyToManyField(Awards,blank=True)
    avg_rating = models.FloatField(default=0)

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name

class Rating(models.Model):
    """
    this class will manage Ratings details and operation on the data related to Ratings
    """
    RATINGS =[('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10')
    ]
    movie_rating = models.CharField(max_length=20,choices=RATINGS,default='0')
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    votes = models.IntegerField(default='0')
    def __str__(self):
        return self.movie.name + str(self.movie_rating) 

    