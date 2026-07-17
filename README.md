# 🛒 ShopCart — Django Shopping Cart Demo

[![Live Demo](https://img.shields.io/badge/LIVE_DEMO-Click_Here-brightgreen)](https://suryanshdev1.pythonanywhere.com/)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-CDN-06B6D4)
![Status](https://img.shields.io/badge/Status-Deployed-success)

> A production-inspired Django e-commerce demo built with clean architecture, modern UI, and full deployment support. Designed as a portfolio project to demonstrate full-stack Python development skills.

---

## 🌐 Live Website

**🔗 [https://suryanshdev1.pythonanywhere.com/](https://suryanshdev1.pythonanywhere.com/)**

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🏠 **Homepage** | Hero section, featured products, new arrivals, category browsing |
| 📦 **Product Catalog** | Browse all products with search, category filter, sorting, and pagination |
| 🔍 **Product Details** | Full product pages with stock info, related products, and add-to-cart |
| 🛒 **Shopping Cart** | Session-based cart with add, remove, update quantity, and total calculation |
| 📱 **Responsive Design** | Modern UI built with Tailwind CSS, works perfectly on mobile and desktop |
| 🔐 **Admin Dashboard** | Full Django admin for managing products, categories, and cart items |
| 📧 **Contact Form** | Professional contact page ready for email backend integration |
| 🐳 **Docker Support** | Complete containerization with Dockerfile and docker-compose.yml |
| ☁️ **Deployed** | Live on PythonAnywhere with HTTPS support |

---

## 🛠 Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 5.0, Python 3.11 |
| **Frontend** | Tailwind CSS (CDN), Font Awesome 6, Google Fonts (Inter) |
| **Database** | SQLite (development), PostgreSQL (Docker) |
| **Containerization** | Docker, Docker Compose |
| **Server** | Gunicorn + WhiteNoise (production-ready) |
| **Deployment** | PythonAnywhere (Free Tier) |

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.11+
- pip
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/shopcart.git
cd shopcart

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create static directories
mkdir -p shop/static/shop/css shop/static/shop/js shop/static/shop/images

# 6. Run migrations
python manage.py makemigrations shop
python manage.py migrate

# 7. Create superuser
python manage.py createsuperuser

# 8. Add sample data (optional)
python manage.py shell
# Paste sample data script from docs/

# 9. Run development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/admin/`

---

## 🐳 Docker Setup

```bash
# Build and run with PostgreSQL
docker-compose up --build

# Run migrations in container
docker-compose exec web python manage.py migrate

# Create superuser in container
docker-compose exec web python manage.py createsuperuser
```

---

## 📁 Project Structure

```
shopcart/
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Multi-container orchestration
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
│
├── shopcart/                  # Project settings
│   ├── __init__.py
│   ├── settings.py           # Django settings (env-based)
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
│
├── shop/                      # Main application
│   ├── __init__.py
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── cart.py               # Session-based cart logic
│   ├── context_processors.py # Global cart context
│   ├── forms.py              # Cart and contact forms
│   ├── models.py             # Product, Category, CartItem models
│   ├── urls.py               # App URL routing
│   ├── views.py              # All page views
│   ├── migrations/           # Database migrations
│   ├── static/shop/          # Static assets (CSS, JS, images)
│   └── templates/shop/       # HTML templates
│       ├── base.html
│       ├── home.html
│       ├── product_list.html
│       ├── product_detail.html
│       ├── cart.html
│       ├── about.html
│       ├── contact.html
│       └── category_detail.html
│
├── media/                     # User uploads (product images)
├── staticfiles/               # Collected static files (production)
└── docs/                      # Technical documentation
```

---

## 🗄️ Database Schema

### Category
| Field | Type | Description |
|-------|------|-------------|
| name | CharField | Category name (unique) |
| slug | SlugField | URL-friendly identifier |
| description | TextField | Category description |
| image | ImageField | Category image |
| is_active | BooleanField | Visibility status |

### Product
| Field | Type | Description |
|-------|------|-------------|
| category | ForeignKey | Product category |
| name | CharField | Product name |
| slug | SlugField | URL-friendly identifier |
| description | TextField | Product description |
| price | DecimalField | Current price |
| old_price | DecimalField | Original price (for sales) |
| image | ImageField | Product image |
| stock | PositiveIntegerField | Available quantity |
| available | BooleanField | In-stock status |
| featured | BooleanField | Homepage display |

### CartItem
| Field | Type | Description |
|-------|------|-------------|
| session_key | CharField | Browser session identifier |
| product | ForeignKey | Linked product |
| quantity | PositiveIntegerField | Item quantity (1-99) |

---

## 🔧 Environment Variables

Create a `.env` file from `.env.example`:

```env
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
```

**Generate a secure secret key:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## 🌐 Deployment Guide (PythonAnywhere)

### 1. Upload Code
- Upload ZIP file or clone from GitHub
- Extract to `/home/username/`

### 2. Setup Virtual Environment
```bash
cd ~
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Web App
- **Source code:** `/home/username`
- **Working directory:** `/home/username`
- **WSGI file:** Configure with environment variables

### 4. Set Static Files
| URL | Directory |
|-----|-----------|
| `/static/` | `/home/username/staticfiles` |
| `/media/` | `/home/username/media` |

### 5. Environment Variables in WSGI
```python
import os
os.environ['DJANGO_SECRET_KEY'] = 'your-secret-key'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'username.pythonanywhere.com'
```

### 6. Migrate & Collect Static
```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### 7. Reload
Click **Reload** button in Web tab.

---

## 📚 Research & Documentation

This project includes comprehensive research:

- **Django Shopping Cart Repositories** — Comparison of 4+ solutions (django-oscar, Saleor, django-cart, django-shop)
- **Django Themes** — Analysis of free/paid themes and integration approaches
- **Joomla to Django Migration** — Complete 11-step migration strategy
- **Technical Documentation** — Architecture, database schema, security considerations

See `docs/` and `research/` folders for full details.

---

## 🔮 Future Improvements

- [ ] User authentication & registration
- [ ] Checkout flow with Stripe/PayPal integration
- [ ] Order history & tracking
- [ ] Product reviews & ratings
- [ ] Wishlist functionality
- [ ] Admin analytics dashboard
- [ ] Multi-language support (i18n)
- [ ] Redis caching layer
- [ ] Celery background tasks
- [ ] REST API with Django REST Framework

---

## 📝 Portfolio Content

### Project Title
**ShopCart — Django E-Commerce Demo**

### Professional Description
A full-featured Django shopping cart application demonstrating modern web development practices including session-based cart persistence, responsive Tailwind CSS design, Docker containerization, and clean MVC architecture. Built as a portfolio-quality project showcasing backend development, frontend design, and DevOps skills.

### Skills Demonstrated
- Django web framework & ORM
- Session management & state persistence
- Database design & relationships
- Docker & container orchestration
- Modern responsive UI/UX design
- Production deployment & configuration
- Technical documentation writing

### Resume Bullet Points
- Built a complete Django e-commerce demo with session-based shopping cart, product catalog, and admin dashboard
- Containerized application with Docker Compose including PostgreSQL database and persistent media volumes
- Designed responsive modern UI using Tailwind CSS with mobile-first approach
- Deployed live production website on PythonAnywhere with HTTPS and environment-based configuration
- Researched and compared 4+ Django e-commerce repositories and 5+ UI themes for technology selection

### Elevator Pitch (30 seconds)
> "I built ShopCart, a Django e-commerce demo that goes beyond tutorials. It features a real session-based shopping cart, product search and filtering, a responsive Tailwind UI, and full Docker containerization. I researched multiple Django cart libraries and chose a lightweight approach to demonstrate my ability to build custom solutions rather than just configure existing packages. It's live and deployed at suryanshdev1.pythonanywhere.com."

---

## 📄 License

MIT License — Free for personal and commercial use.

---

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) — The web framework for perfectionists
- [Tailwind CSS](https://tailwindcss.com/) — Utility-first CSS framework
- [Font Awesome](https://fontawesome.com/) — Icons library
- [PythonAnywhere](https://www.pythonanywhere.com/) — Free Python hosting

---

## 📬 Contact

- **Live Website:** [https://suryanshdev1.pythonanywhere.com/](https://suryanshdev1.pythonanywhere.com/)
- **GitHub:** [github.com/yourusername/shopcart](https://github.com/yourusername/shopcart)

---

<p align="center">
  <b>Built with ❤️ using Django & Tailwind CSS</b>
</p>
