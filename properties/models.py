from django.db import models
from django.urls import reverse

# Create your models here.
class Properties(models.Model):
    PropertyName = models.CharField(max_length=255, help_text="The Name of the property")
    Address = models.CharField(max_length=255, help_text="The address of the above property")
    City = models.CharField(max_length=255, help_text="The city where the property is located")
    County = models.CharField(max_length=100, help_text="The county of the city above")
    Picture1 = models.ImageField(help_text="Attach first image of your property")
    Picture2 = models.ImageField(help_text="Attach second image of your property", blank=True, null=True)
    Picture3 = models.ImageField(help_text="Attach third image of your property", blank=True, null=True)
    Picture4 = models.ImageField(help_text="Attach fourth image of your property", blank=True, null=True)

    def __str__(self):
        return self.PropertyName

    def get_absolute_url(self):
        return reverse('home')

