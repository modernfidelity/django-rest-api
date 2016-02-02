from django.contrib import admin

# Register your models here.
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "strapline", "date_start", "date_end")


admin.site.register(Event, EventAdmin)