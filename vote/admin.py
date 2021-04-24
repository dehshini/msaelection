from django.contrib import admin
from .models import Candidate, Vote, Category


# Register your models here.
admin.site.register(Candidate)
admin.site.register(Vote)
admin.site.register(Category)
