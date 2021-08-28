from django.contrib import admin
from . models import Movies,Artist,Awards,Rating

"""
here i am registering my models of this app
"""
admin.site.register(Movies)
admin.site.register(Awards)
admin.site.register(Artist)
admin.site.register(Rating)