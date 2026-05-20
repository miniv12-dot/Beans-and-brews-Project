# ☕ Beans & Brews — Full-Stack Coffee E-Commerce & Barista Command Center

A modern, responsive full-stack e-commerce web application designed to connect premium coffee shop customers with real-time barista kitchen operations. Built with a highly optimized Python/Django core, a PostgreSQL relational database backend, and synchronous JavaScript state tracking engines.

---

## 🚀 Key Architectural Features

* **Real-Time Asynchronous Progress Tracker:** Engineered a live customer tracking interface that uses JavaScript `fetch` asynchronous polling loops to monitor backend database mutations and transition order status visual steps without requiring page reloads.
* **Smart "Order My Usual" Reordering:** Developed an optimized PostgreSQL query using Django ORM's relational aggregation matrix (`Count` and `annotate`) to automatically analyze customer order histories and instantly deliver a one-click dashboard shortcut banner for their most frequently purchased item.
* **Barista Operations Command Center:** Designed a secure, internal, live kitchen workflow pipeline allowing staff users to manage incoming preparing queues and clear out orders dynamically.
* **Advanced Relational Database Design:** Normalized schemas spanning multi-table dependencies, including automated model instance total property calculations (`grand_total`, `line_total`) running across Many-to-One architectures.
* **Premium Cohesive UX System:** Hand-crafted a sleek, lightweight, custom CSS storefront design optimized for fluid navigation and state preservation.

---

## 🛠️ The Tech Stack

* **Backend Framework:** Django 6.0.5
* **Runtime Language:** Python 3.14.3
* **Database Engine:** PostgreSQL
* **Frontend Layers:** HTML5, Custom CSS3, Vanilla JavaScript (AJAX / JSON Interactivity)
* **Session Handler:** Django Middleware Engine (Secure client-side cart states)

---

## 🗄️ Database Architecture Model Blueprints

### 1. Order Model
Tracks distinct billing invoices and structural state tags for customer orders.
* `user`: ForeignKey $\rightarrow$ Django User Model
* `first_name` / `last_name` / `email`: CharFields / EmailField
* `created_at`: DateTimeField (auto_now_add=True)
* `status`: CharField (Tracks state: e.g., "Preparing" $\rightarrow$ "Ready for Collection! ☕")

### 2. OrderItem Model
Handles specific drink itemizations and quantities assigned to order transactions.
* `order`: ForeignKey $\rightarrow$ `Order` (Cascade relation via related_name='items')
* `drink`: ForeignKey $\rightarrow$ `Drink`
* `price`: DecimalField (max_digits=5, decimal_places=2)
* `quantity`: IntegerField

---

## 💻 Local Quickstart Installation

Follow these steps to spin up the server environment locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/beans-and-brews.git](https://github.com/YOUR_USERNAME/beans-and-brews.git)
   cd beans-and-brews