from django.contrib import admin
from demo01.models import *

# Register your models here.


@admin.register(Category)
class CategoryInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Post)
class PostInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category', 'title', 'body', 'date']
