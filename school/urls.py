from django.http import HttpResponse
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('',views.index,name='index'),
    path('event_list', views.event_list, name='event_list'),
    path('gallery/',views.gallery_view,name='gallery'),
    path('upload/',views.upload_photo,name='upload_photo'),
    path('contact/',views.contact_view, name='contact'),
    path('testimonials/',views.testimonials_view, name='testimonials'),
    path('success/', lambda request: HttpResponse(' # type: ignoreThank you for your message!'), name='success'),
    path('tlc/', views.tlc_view, name='tlc'),
    path('strataford', views.startaford_view, name='strataford'),
    path('superuser-panel/', admin.site.urls),  
    path('superuser-access/', views.superuser_access, name='superuser_access'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
