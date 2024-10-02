from django.contrib import admin
from .models import photo,Event,SchoolCal,testimonials,Term,term_events

admin.site.register(photo)
admin.site.register(Event)
admin.site.register(testimonials)
admin.site.register(term_events)
admin.site.register(Term)

@admin.register(SchoolCal)
class SchoolCalAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
