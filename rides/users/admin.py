from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Ride, RideEvent


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ['rider', 'driver', 'status']


@admin.register(RideEvent)
class RideEvent(admin.ModelAdmin):
    ...
