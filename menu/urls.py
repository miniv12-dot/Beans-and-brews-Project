from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 1. Core Pages
    path('', views.home, name='home'),
    path('drink/<int:drink_id>/', views.drink_detail, name='drink_detail'),
    
    # 2. Cart & Checkout Operations
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:drink_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:drink_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:drink_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    
    # 3. Authentication Routes
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='menu/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # 4. User Profile & Account Management
    path('my-orders/', views.my_orders, name='my_orders'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='menu/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='menu/password_change_done.html'), name='password_change_done'),
    
    # 5. Barista / Staff Operations
    path('staff/dashboard/', views.barista_dashboard, name='barista_dashboard'),
    path('staff/complete/<int:order_id>/', views.complete_order, name='complete_order'),
    path('order/status/<int:order_id>/', views.check_order_status, name='check_order_status'),
]