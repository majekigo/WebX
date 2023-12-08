from django.contrib import admin
from .models import Category, Tag, Product, Order, OrderPosition


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    list_display = ('name', 'description', 'price', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('category__name', 'tags__name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'order_date', 'customer_name', 'customer_phone')
    inlines = [OrderPositionInline]


@admin.register(OrderPosition)
class OrderPositionAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'discount')
