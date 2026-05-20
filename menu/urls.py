from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('drink/<int:drink_id>/', views.drink_detail, name='drink_detail'),
    path('cart/add/<int:drink_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    
    # THE NEW CHECKOUT ROUTE
    path('checkout/', views.checkout, name='checkout'),
]
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.home, name='home_by_category'),
    path('drink/<int:drink_id>/', views.drink_detail, name='drink_detail'),
    path('drink/<int:drink_id>/', views.drink_detail, name='drink_detail'),
    path('cart/add/<int:drink_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    
    # NEW AUTHENTICATION ROUTES:
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='menu/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='menu/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # THE NEW PROFILE ROUTE
    path('my-orders/', views.my_orders, name='my_orders'),
    # NEW CART MANIPULATION ROUTES:
    path('cart/update/<int:drink_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:drink_id>/', views.remove_from_cart, name='remove_from_cart'),
    # BARISTA STAFF CHANNELS
    path('staff/dashboard/', views.barista_dashboard, name='barista_dashboard'),
    path('staff/complete/<int:order_id>/', views.complete_order, name='complete_order'),
    path('order/status/<int:order_id>/', views.check_order_status, name='check_order_status'),



]
