# ☕ Beans & Brews — Full-Stack Coffee E-Commerce & Barista Command Center

A modern, responsive full-stack e-commerce web application designed to bridge the gap between premium coffee shop customers and real-time barista kitchen operations. Built with a highly optimized Python/Django core, a resilient PostgreSQL relational database backend, and clean client-side state engines.

---

## 🛠️ The Tech Stack

Component | Technology Used
--- | ---
**Backend Core** | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
**Database Engine** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
**Frontend Architecture** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
**Session & Storage** | Django Middleware Engine & Cloudinary

---

## 📸 System Showcase

| 🌓 Dual-Theme Engine | 👤 Frictionless Guest Flow |
| --- | --- |
| ![Theme Engine](/beans_and_brews/images/theme-toggle.gif) | ![Guest Checkout Flow](/beans_and_brews/images/guest-checkout.png) |

| ☕ Barista Command Center |
| --- |
| ![Live Barista Dashboard](/beans_and_brews/images/barista-dashboard.png) |

---

## 🚀 Key Architectural Highlights

### ⚡ Real-Time Asynchronous Progress Tracker
> Engineered a live customer tracking interface utilizing JavaScript `fetch` asynchronous polling loops. This monitor tracks backend database mutations directly, updating order status visual steps seamlessly without forcing an expensive browser page reload.

### 👤 Hybrid Session-Based State Management
> Implemented a bulletproof guest checkout framework driven by Django Sessions. It isolates customer data securely, mitigating cart overlaps across distinct guests, while seamlessly shifting to persistent database-backed history profiles the moment a user authenticates.

### 🌓 Reactive Theme Engine
> Developed a lightweight, state-driven UI featuring custom CSS variables synchronized with browser `localStorage`. Shifting between a crisp Ivory Light Mode and a rich Espresso Dark Mode performs instantly with absolute zero layout flashing.

### 📊 Smart "Order My Usual" Reordering
> Authored an optimized PostgreSQL query leveraging the Django ORM's relational aggregation matrix (`Count` and `annotate`). The system dynamically cross-references user histories to immediately surface a single-click shortcut dashboard button for their most frequently purchased beverage.

### ⚙️ Advanced Relational Schema Design
> Normalized complex data architectures spanning multi-table dependencies, including automatic inline property calculators (`grand_total`, `line_total`) executing smoothly across structured Many-to-One architectures.

---

## 🗄️ Database Blueprints

### 1. Order Model
Tracks distinct billing invoices and structural state tags for customer orders.
* `user`: ForeignKey $\rightarrow$ Django User Model *(Gracefully handles `null=True` for Guest operations)*
* `first_name` / `last_name` / `email`: Fields dynamically populated by session context or user accounts.
* `status`: CharField tracking the live pipeline State: `Preparing` $\rightarrow$ `Ready for Collection! ☕`

### 2. OrderItem Model
Handles individual drink itemization and pricing history assigned to order transactions.
* `order`: ForeignKey $\rightarrow$ `Order` *(Configured with a clean `on_delete=models.CASCADE` via `related_name='items'`)*
* `drink`: ForeignKey $\rightarrow$ `Drink`
* `price`: DecimalField tracking exact checkout point cost configuration.

---

## 💻 Local Quickstart Installation

Spin up the server environment locally on your native machine in minutes:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/miniv12-dot/Beans-and-brews-Project](https://github.com/miniv12-dot/Beans-and-brews-Project)
   cd beans-and-brews
   Establish your virtual environment:

2. **Establish your virtual environment:**
   Bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   Install dependencies:

3. **Install dependencies:**
   Bash
   pip install -r requirements.txt
   Initialize database & boot server:

4. **Initialize database & boot server:**
   Bash
   python manage.py migrate
   python manage.py runserver`

👨‍💻 Author
Minenhle Bhengu

LinkedIn: Minenhle Bhengu