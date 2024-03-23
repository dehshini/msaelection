from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Candidate, Vote, Category

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Vote)
admin.site.register(Category)

#admin.site.register(User, CustomUserAdmin)

