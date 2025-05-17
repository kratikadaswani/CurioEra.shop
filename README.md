# CurioEra.shop
CURIO ERA is a vintage-inspired ecommerce website that lets users discover, admire, and purchase timeless collectibles — from cassettes and vintage phone covers to classic almirahs and delicate flower décor. The website is designed with nostalgic aesthetics, featuring a hero section, gallery, interactive polls, and a live offer timer to engage users. Built using Django and Bootstrap, it serves as a responsive, cleanly organized, and scalable web platform.

This web application lets users:
- Browse vintage products
- Register and log in to a personalized experience
- Participate in a poll for preferred products and could upload their aesthetic vintage image and memory to get featured
- View product details, add to cart, and checkout
- Experience a classic '90s showcase vibe digitally
- Download the corresponding invoice after checkout
- Interactive chatbot feature for any customer queries
  
Tech Stack-
Backend- Python 3.11+, Django 4.x
Frontend-Bootstrap 4.6, HTML5, CSS3, JavaScript
Database-SQLite3 (default Django database)

Project Setup & Installation-
    Prerequisites-
   1. Python 3.11+
   2. pip (Python package installer)
   3. virtualenv (optional but recommended)
   4. Pillow (for static files)

  # Clone the repository  
  git clone [https://github.com/yourusername/curio-era.git](https://github.com/kratikadaswani/CurioEra.shop.git)
  
  # Move into project directory  
  cd ecomsite
  
  # (Optional) Create and activate virtual environment  
  python -m venv env  
  source env/bin/activate  # macOS/Linux  
  env\Scripts\activate     # Windows  
  
  # Install required dependencies  
  pip install -r requirements.txt  

Project Structure 

ECOMSITE/                          # main project folder
├── ecom/                       # Django project settings module
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py                 # include home.urls and shop.urls
│   ├── wsgi.py
│   └── __pycache__/
│
├── home/                       # 'home' app
│   ├── __pycache__/
│   ├── migrations/
│   ├── static\
│   │   └── home/
│   │       └── (static files like CSS, JS, images)
│   ├── templates\
│   │   └── home/
│   │       ├── cabinet.html
│   │       ├── home.html
│   │       ├── login_page.html
│   │       └── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/imgs                     # for user-uploaded images/files
│
├── shop/                       # 'shop' app
│   ├── __pycache__/
│   ├── migrations/
│   ├── static\
│   │   └── shop/
│   │       └── style.css
│   ├── templates\
│   │   └── shop/
│   │       ├── base.html
│   │       ├── checkout.html
│   │       ├── details.html
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3                  # database
├── manage.py
└── (optional) ecomenv/         # virtual environment 

# Run Django migrations  
python manage.py migrate  

# Start the development server  
python manage.py runserver  
Visit http://127.0.0.1:8000/ in your browser.

Future Improvements-
1. Integrate payment gateway (Razorpay/PayPal)
2. Track poll analytics
