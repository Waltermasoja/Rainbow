from django import template
from django.conf import settings
import os

register = template.Library()

@register.filter
def check_image(value):
    file_path = os.path.join(settings.MEDIA_ROOT, value)
    if not os.path.isfile(file_path):
        return 'default_image.jpg'
    return value