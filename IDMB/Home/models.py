"""
home app will handle all the data of IDMB in this model file
"""
from django.db import models

# Create your models here.
class Movies(models.Model):
    """
    this class will manage movies details and operation on the data related to movies 
    """
    pass
class Artist(models.Model):
    """
    this class will manage Artist details and operation on the data related to Artist
    """
    pass

class Awards(models.Model):
    """
    this class will manage Awards details and operation on the data related to Awards
    """
    pass


class Rating(models.Model):
    """
    this class will manage Ratings details and operation on the data related to Ratings
    """
    pass