from django.contrib import admin
from .models import Drink, Order, OrderItem, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # This automatically fills out the slug field as you type the category name!
    prepopulated_fields = {'slug': ('name',)}

# This is a cool feature! It lets us display the items inside the Order page
# instead of making you click into a completely separate page for items.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['drink']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Replaced 'is_paid' with our new 'status' field
    list_display = ['id', 'first_name', 'last_name', 'email', 'status', 'created_at'] 
    list_filter = ['status', 'created_at']

# Register the Drink model normally
admin.site.register(Drink)