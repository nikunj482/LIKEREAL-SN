from django.contrib import admin
from .models import person

class personAdmin(admin.ModelAdmin):
    list_display = ("username","fullname","email","phone","gender",)
admin.site.register(person, personAdmin)
