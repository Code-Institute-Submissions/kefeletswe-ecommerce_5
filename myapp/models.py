from django.db import models


# Create your models here. anything to do with our shopping cart
class Category(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
  

    class Meta:
        verbose_name_plural = 'Categories'
    ordering = ('-created')# i put - sign so i can sort by ascending and descending, specify how we can order,   
  
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Products(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
   #  image = models.ImageField(upload_to='uploads/products/')
    in_stock = models.BooleanField(default=True)
    

 
    def __str__(self):
        return self.title



