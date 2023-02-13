from django.contrib import admin

from hotel_shared.models import HotelType


# Register your models here.
@admin.register(HotelType)
class HotelTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
