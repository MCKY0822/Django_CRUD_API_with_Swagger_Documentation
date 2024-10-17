from django.contrib import admin
from .models import TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('day', 'start', 'stop', 'ids')
    list_filter = ('day',)
    search_fields = ('day', 'ids')
