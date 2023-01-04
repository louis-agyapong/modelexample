from django.contrib import admin
from .models import Framework, Language, Movie, Character

admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Movie)
admin.site.register(Character)
