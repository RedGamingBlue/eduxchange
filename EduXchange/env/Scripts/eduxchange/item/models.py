from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    descriprion = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created at = models.DateTimeField(auto_noe_add=True)
