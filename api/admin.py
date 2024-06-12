from django.contrib import admin
from .models import Item

@admin.register(Item)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')