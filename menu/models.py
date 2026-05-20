from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    # a slug is a URL-friendly version of the name (e.g., "Hot Drinks" becomes "hot-drinks")
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Drink(models.Model):
    # NEW: Link each drink to a specific category. 
    # null=True, blank=True prevents errors with your existing drinks during the migration.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='drinks')
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='drinks/', null=True, blank=True)

    def __str__(self):
        return self.name



# Your existing Drink model stays here...

# --- NEW CODE BELOW ---

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # STATUS BELONGS HERE!
    status = models.CharField(max_length=50, default="Preparing") 

    @property
    def grand_total(self):
        return sum(item.line_total for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.first_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=1)

    # MAKE SURE THERE IS NO STATUS FIELD HERE!

    @property
    def line_total(self):
        return self.price * self.quantity