from django.db import models

class Restaurant(models.Model): 
    name = models.CharField("Name", max_length=50) 
    address = models.TextField("Address", max_length=100) 
    def __str__(self): 
        return self.name 
    class Meta: 
        verbose_name = "Restaurant" 
        verbose_name_plural = "Restaurants"