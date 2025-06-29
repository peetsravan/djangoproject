# 📱 Next Labs – Android-Rewards Platform

A Django 5.2 project where:

* **Admin-Facing panel** (custom UI, _not_ default Django Admin)  
  * Add / edit Android apps  
  * Specify reward points users earn for downloading each app  
  * Review user-submitted screenshots for verification

* **User-Facing portal**  
  * Signup / Login (JWT or django-allauth – your choice)  
  * See their profile (name, total points, tasks completed)  
  * Browse all apps & their point values  
  * Drag-and-drop a screenshot to prove they launched the app and claim points

---

## ⚙️ Tech Stack

| Area | Choice |
|------|--------|
| Backend | Django 5.2, Django REST Framework |
| Auth | `django-allauth` + JWT (`djangorestframework-simplejwt`) |
| DB | PostgreSQL |
| Storage | Local `media/` (S3 ready) |
| Frontend | HTMX + Tailwind (simple) or React (optional) |
| File upload UX | Dropzone.js |

---

## 🛠️ Local Development Setup

### 1  Clone

```bash
git clone https://github.com/yourusername/djangoproject-main.git
cd djangoproject-main
```

### 2  Virtual env

```bash
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
```

### 3  Install deps

```bash
pip install -r requirements.txt
```

### 4  Environment variables (`.env`)

```bash
cp .env.example .env
# then edit:
# DEBUG=True
# SECRET_KEY=change-me
# DATABASE_*  …
# ALLOWED_HOSTS=127.0.0.1,localhost
```

_(Uses **django-environ** – already listed in `requirements.txt`.)_

### 5  PostgreSQL DB

```sql
CREATE DATABASE next_labs;
```

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6  Run server

```bash
python manage.py runserver
```

Visit <http://localhost:8000>

---

## 👩‍💻 Developer Contribution Steps

> For team members working on feature branches

### 1. Checkout new feature branch

```bash
git checkout -b feature/<your-feature-name>
```

### 2. Add new app (optional)

```bash
python manage.py startapp my_app
```

Then register it in `settings.py` → `INSTALLED_APPS`

### 3. Create models & migrations

```bash
python manage.py makemigrations my_app
python manage.py migrate
```

### 4. Run locally and test

```bash
python manage.py runserver
```

### 5. Run tests (if any)

```bash
python manage.py test
```

### 6. Commit and push

```bash
git add .
git commit -m "Added <feature>"
git push origin feature/<your-feature-name>
```

---

## 🚀 Deployment Guide (Ubuntu 20.04 + Gunicorn + Nginx)

1. Install packages  
2. Clone repo to `/home/ubuntu/next_labs`  
3. `python3 -m venv env && source env/bin/activate && pip install -r requirements.txt`  
4. Upload `.env.production` (with `DEBUG=False`)  
5. Systemd unit:

   ```ini
   Environment="DJANGO_ENV_FILE=.env.production"
   ExecStart=/home/ubuntu/next_labs/env/bin/gunicorn \
             --workers 3 \
             --bind unix:/home/ubuntu/next_labs/gunicorn.sock \
             next_labs.wsgi:application
   ```

6. Nginx reverse-proxy & serve `/static/` + `/media/`  
7. (Optional) HTTPS via Let’s Encrypt `certbot`

---

## ✅ Common Management Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py collectstatic
```

---

## 🧩 Next Steps / Improvements

* Docker-compose with `env_file: .env`
* Celery + Redis for async screenshot processing
* S3 / CloudFront for production media
* GitHub Actions CI pipeline (flake8 + tests)

---

## 👨‍💻 Author

Your Name — [LinkedIn](https://www.linkedin.com/in/yourprofile)