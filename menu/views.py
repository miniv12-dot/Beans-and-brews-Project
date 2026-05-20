from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.http import JsonResponse
from django.db.models import Count
from .models import Drink, Order, OrderItem, Category
from .forms import CustomRegisterForm

# 1. The Home Page View (UPDATED: With "Order My Usual" Optimization)
def home(request, category_slug=None):
    all_drinks = Drink.objects.all()
    categories = Category.objects.all() # Fetch all categories for the filter nav
    selected_category = None
    usual_drink = None

    # Check if a specific category slug was passed through the URL
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        all_drinks = all_drinks.filter(category=selected_category)
        
    # NEW LOGIC: Compute the customer's most ordered menu item from PostgreSQL
    if request.user.is_authenticated:
        favorite_drink_query = OrderItem.objects.filter(order__user=request.user) \
            .values('drink') \
            .annotate(drink_count=Count('drink')) \
            .order_by('-drink_count') \
            .first()
        
        if favorite_drink_query:
            usual_drink = Drink.objects.filter(id=favorite_drink_query['drink']).first()
        
    context = {
        'drinks': all_drinks,
        'categories': categories,
        'selected_category': selected_category,
        'usual_drink': usual_drink # Injected into template payload context
    }
    return render(request, 'menu/index.html', context)


# 2. The Single Drink Detail View
def drink_detail(request, drink_id):
    single_drink = get_object_or_404(Drink, pk=drink_id)
    context = {'drink': single_drink}
    return render(request, 'menu/drink_detail.html', context)


# 3. Add to Cart View
def add_to_cart(request, drink_id):
    drink = get_object_or_404(Drink, pk=drink_id)
    cart = request.session.get('cart', {})
    drink_id_str = str(drink_id)

    if drink_id_str in cart:
        cart[drink_id_str]['quantity'] += 1
    else:
        cart[drink_id_str] = {
            'name': drink.name, 
            'price': str(drink.price), 
            'quantity': 1
        }
    
    request.session['cart'] = cart
    return redirect('cart_detail')


# 4. View the Cart View
def cart_detail(request):
    cart = request.session.get('cart', {})
    total_price = 0
    for item in cart.values():
        total_price += float(item['price']) * item['quantity']
        
    # Fetch all available drinks from Postgres so the user can see options to add!
    other_drinks = Drink.objects.filter(is_available=True)
        
    context = {
        'cart': cart, 
        'total_price': total_price,
        'other_drinks': other_drinks
    }
    return render(request, 'menu/cart_detail.html', context)


# 5. The Checkout View
def checkout(request):
    cart = request.session.get('cart', {})
    
    if not cart:
        return redirect('home')
        
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        user_email = request.POST.get('email')
        
        new_order = Order.objects.create(
            first_name=f_name,
            last_name=l_name,
            email=user_email
        )
        
        if request.user.is_authenticated:
            new_order.user = request.user
            new_order.save()
            
            request.user.first_name = f_name
            request.user.last_name = l_name
            request.user.email = user_email
            request.user.save()
            
        for drink_id, item in cart.items():
            drink_obj = Drink.objects.get(id=int(drink_id))
            OrderItem.objects.create(
                order=new_order,
                drink=drink_obj,
                price=float(item['price']),
                quantity=item['quantity']
            )
            
        request.session['cart'] = {}
        return render(request, 'menu/order_success.html', {'order': new_order})
        
    return render(request, 'menu/checkout.html', {'cart': cart})


# 6. Customer Registration View
def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomRegisterForm()
    return render(request, 'menu/register.html', {'form': form})


# 7. Customer Dashboard View
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'menu/my_orders.html', {'orders': orders})


# 8. Update Cart Item Quantity View
def update_cart(request, drink_id, action):
    cart = request.session.get('cart', {})
    drink_id_str = str(drink_id)
    
    if drink_id_str in cart:
        if action == 'increment':
            cart[drink_id_str]['quantity'] += 1
        elif action == 'decrement':
            cart[drink_id_str]['quantity'] -= 1
            if cart[drink_id_str]['quantity'] <= 0:
                del cart[drink_id_str]
                
    request.session['cart'] = cart
    return redirect('cart_detail')


# 9. Remove Item Completely View
def remove_from_cart(request, drink_id):
    cart = request.session.get('cart', {})
    drink_id_str = str(drink_id)
    
    if drink_id_str in cart:
        del cart[drink_id_str]
        
    request.session['cart'] = cart
    return redirect('cart_detail')


# 10. The Private Barista Operations Dashboard
@user_passes_test(lambda u: u.is_staff)
def barista_dashboard(request):
    active_orders = Order.objects.filter(status="Preparing").order_by('created_at')
    return render(request, 'menu/barista_dashboard.html', {'orders': active_orders})


# 11. The Database Status Updater Action
@user_passes_test(lambda u: u.is_staff)
def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "Ready for Collection! ☕"
    order.save()
    return redirect('barista_dashboard')


# 12. Background endpoint to check order status without reloading the page
def check_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return JsonResponse({'status': order.status})