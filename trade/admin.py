from django.contrib import admin


from .models import Product,Category,Comment



class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "description", "created", "updated"]
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["product", "brand", "type"]

class Commentadmin(admin.ModelAdmin):
    list_display = ["name", "product", "comment"]

inlines = [ProductAdmin,CategoryAdmin,Commentadmin]
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, Commentadmin)


