from django.contrib import admin
from .models import photo,Event,SchoolCal,testimonials,Term,term_events
from .models import Gallery, Image


admin.site.register(photo)
admin.site.register(Event)
admin.site.register(testimonials)
admin.site.register(term_events)
admin.site.register(Term)
admin.site.register(Gallery)
admin.site.register(Image)

@admin.register(SchoolCal)
class SchoolCalAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
