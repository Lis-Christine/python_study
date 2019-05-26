from django.contrib import admin
from .models import Category, Board, Good

# Register your models here.
admin.site.register(Category)
admin.site.register(Board)
admin.site.register(Good)