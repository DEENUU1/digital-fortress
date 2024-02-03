from django.contrib import admin
from .models import Product, ProductPrice, UserSubscription


class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('value', 'currency')
    list_filter = ('currency',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_project_storage', 'num_of_projects', 'is_active')
    list_filter = ('price', 'num_of_projects', 'max_project_storage', 'is_active')


class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'is_active', 'is_expired')
    list_filter = ('product', 'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)
admin.site.register(UserSubscription, UserSubscriptionAdmin)