import os
import django

# 1. Tell Python where your Django settings file lives
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beans_and_brews.settings')
django.setup()

# 2. Import your models after Django is initialized
from menu.models import Category, Drink

def seed_database():
    print("🧹 Cleaning out old menu data...")
    Drink.objects.all().delete()
    Category.objects.all().delete()

    print("🌱 Creating new Categories...")
    hot_brews = Category.objects.create(name="Hot Brews", slug="hot-brews")
    iced_coffees = Category.objects.create(name="Cold Iced Coffees", slug="cold-iced-coffees")
    pastries = Category.objects.create(name="Fresh Pastries", slug="fresh-pastries")

    print("☕ Creating Drink and Menu Items...")
    
    # --- HOT BREWS ---
    Drink.objects.create(
        category=hot_brews,
        name="Cappuccino",
        price=32.00,
        description="A perfectly balanced espresso shot topped with smooth, velvety steamed milk foam.",
        is_available=True
    )
    Drink.objects.create(
        category=hot_brews,
        name="Spicy Latte",
        price=38.00,
        description="Our signature rich espresso with textured milk, infused with cinnamon and a hint of warm cayenne pepper.",
        is_available=True
    )
    Drink.objects.create(
        category=hot_brews,
        name="Mocha",
        price=35.00,
        description="It is green full of life, milk, coffee, sugar and everything nice.",
        is_available=True
    )
    Drink.objects.create(
        category=hot_brews,
        name="White Latte",
        price=30.00,
        description="Smooth, creamy vanilla sugar money bliss in a cup.",
        is_available=True
    )

    # --- COLD ICED COFFEES ---
    Drink.objects.create(
        category=iced_coffees,
        name="Iced Americano",
        price=28.00,
        description="Chilled espresso shots topped with cold water and served crisp over clear ice blocks.",
        is_available=True
    )
    Drink.objects.create(
        category=iced_coffees,
        name="Amapiano Shake",
        price=45.00,
        description="A heavy-hitting blended iced coffee milkshake, packed with condensed milk, cold brew, and biscuit crumbs.",
        is_available=True
    )

    # --- PASTRIES ---
    Drink.objects.create(
        category=pastries,
        name="Plain Croissant",
        price=25.00,
        description="Flaky, golden-brown puff pastry baked fresh daily with rich French butter.",
        is_available=True
    )
    Drink.objects.create(
        category=pastries,
        name="Choc Muffin",
        price=28.00,
        description="A deep, double-chocolate chip muffin with a soft gooey center.",
        is_available=True
    )

    print("🎉 Database successfully seeded with dummy data!")

if __name__ == '__main__':
    seed_database()