from django.contrib import admin

# Register your models here.
from .models import UserProfile  #打开models.py 的Job class
from .forms import UserForm  #打开models.py 的Job class
# Register your models here.
admin.site.register(UserProfile)
