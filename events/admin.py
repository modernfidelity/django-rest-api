from django.contrib import admin

# Register your models here.
from .models import Event


#
class EventAdmin(admin.ModelAdmin):
    """
    "img_thumb" see models.py
    """
    list_display = ("title", "strapline", "date_start", "date_end", "img_thumb")

    # readonly_fields = ("img_thumb",)


admin.site.register(Event, EventAdmin)
