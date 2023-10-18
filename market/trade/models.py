from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return self.name
    


class Category(models.Model):
    brand = models.CharField(max_length=200, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    TYPE_CHOICES = (
       ("Iphones", "Iphone"),
       ("Andriods", "Andriods"), 
       ("Keypads", "Keypads"), 
       ("Laptops", "Laptops"),
       ("Radio", "Radio"),
       ("Earbuds", "Earbuds"),
       ("Television", "Television"),
       ("Others", "Others"),
       )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="Others")
    # brand_image = models.ImageField(upload_to="trade/images")

    def __str__(self):
        return self.brand
    
    def __str__(self):
        return self.type

class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)