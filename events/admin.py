from django.contrib import admin
from .models import Users, Category, SubCategory, Location, Events

# Register your models here.
admin.site.register(Events)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Users)
