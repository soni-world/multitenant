from django.contrib import admin

from hotel_tenant.models import Hotel


# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name',)
