from django.contrib import admin

from products.models import ProductModel, FormModel, CategoryModel





@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    pass





@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title', 'price']
    list_filter = ['created_at']


@admin.register(FormModel)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age', 'comment']