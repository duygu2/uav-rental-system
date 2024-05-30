from django.db import models

class Brand(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self) :
        return self.name
    
class Category(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self) :
        return self.name


class Uavs(models.Model):
    uavName= models.CharField(max_length=150)
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE)
    model= models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.brand} {self.model}"