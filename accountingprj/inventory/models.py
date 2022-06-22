from django.db import models

# Create your models here.
class Inventory(models.Model):
    inventory_name=models.CharField(max_length=30)
    inventory_location=models.CharField(max_length=100)
    inventory_Description=models.TextField()
    #inventory_creator
    #inventory_create_time