from django.db import models

class photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Event(models.Model):
    title = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title   
from django.db import models

class SchoolCal(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class testimonials(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField()
    def __str__(self):
        return self.name
    

    
class Term(models.Model):
    name = models.CharField(max_length=100)  # e.g., "First Term"
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

class term_events(models.Model):
    term = models.ForeignKey(Term, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g., "Parents Day"
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
#Gallary for Adventure walks.
  
class adwalks_photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
    
#Gallery that is partitioned to have each event with its own gallery
# 
class Gallery(models.Model): 
    name = models.CharField(max_length=100)  
    description = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    gallery = models.ForeignKey(Gallery,related_name='images',on_delete=models.CASCADE)   
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title