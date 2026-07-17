# 🛒 ShopCart — Django Shopping Cart Demo

A production-inspired Django e-commerce demo built with clean architecture, modern UI, and Docker support.

![Django](https://img.shields.io/badge/Django-5.0-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Tailwind](https://img.shields.io/badge/Tailwind-CDN-06B6D4)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)

## ✨ Features

- **Product Catalog** — Browse products with categories, search, sorting, and pagination
- **Shopping Cart** — Session-based cart with add, remove, update quantity, and total calculation
- **Product Details** — Full product pages with related products and stock management
- **Responsive Design** — Modern UI built with Tailwind CSS
- **Admin Dashboard** — Full Django admin for managing products, categories, and cart items
- **Docker Support** — Complete containerization with PostgreSQL

## 🚀 Quick Start

### Local Development

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Create superuser
python manage.py createsuperuser

# 5. Run server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/admin/`

### Docker Setup

```bash
docker-compose up --build
```

## 📁 Folder Structure

```
shopcart-portfolio/
├── manage.py              # Django management script
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── shopcart/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/                  # Main application
│   ├── models.py
│   ├── views.py
│   ├── cart.py
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
│   ├── context_processors.py
│   ├── migrations/
│   ├── static/shop/
│   └── templates/shop/
├── media/                 # User uploads
└── docs/
```

## 📄 License

MIT License
