from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model): 
    name = models.CharField("Name", max_length=50) 
    address = models.TextField("Address", max_length=150) 
    def __str__(self): 
        return self.name 
    class Meta: 
        verbose_name = "Restaurant" 
        verbose_name_plural = "Restaurants"

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name 
    class Meta: 
        verbose_name = "Dish" 
        verbose_name_plural = "Dishes"

class Order(models.Model):

    STATUS_CHOICES = [
    ('new', 'New'),
    ('accepted', 'Accepted'),
    ('delivering', 'Delivering'),
    ('done', 'Done'),
    ] 
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    dishes = models.ManyToManyField(Dish, related_name='orders')
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.id} — {self.customer.username}"