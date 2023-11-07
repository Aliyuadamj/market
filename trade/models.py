from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)

class Product(BaseModel):
    name = models.CharField(max_length=20,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.name
    


class Category(BaseModel):
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

    class Meta:
        verbose_name_plural = 'Categories'

class Comment(BaseModel):
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)