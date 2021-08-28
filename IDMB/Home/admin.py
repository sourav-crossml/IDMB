from django.contrib import admin
from . models import Movies,Artist,Awards,Rating
# Register your models here.

admin.site.register(Movies)
admin.site.register(Awards)
admin.site.register(Artist)
admin.site.register(Rating)