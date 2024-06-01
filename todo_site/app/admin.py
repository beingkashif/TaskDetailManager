from django.contrib import admin
from .models import app
# Register your models here.

admin.register(app)
# class todoAdmin(admin.ModelAdmin):
#     list_display=['id','title', 'details']
