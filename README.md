# Django Commands Reference & Project Setup Guide

## Prerequisites
- Python 3.8+ installed
- pip package manager
- Virtual environment tool (venv, virtualenv, or conda)

## Creating a Fresh Django Project

### 1. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv myproject_env

# Activate virtual environment
# On Windows:
myproject_env\Scripts\activate
# On macOS/Linux:
source myproject_env/bin/activate
```

### 2. Install Django
```bash
# Install latest Django version
pip install django

# Install specific version (optional)
pip install django==4.2

# Verify installation
django-admin --version
```

### 3. Create Django Project
```bash
# Create new project
django-admin startproject myproject

# Navigate to project directory
cd myproject

# Create project in current directory (optional)
django-admin startproject myproject .
```

### 4. Initial Setup
```bash
# Run initial migrations
python manage.py migrate

# Create superuser account
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## Essential Django Management Commands

### Project Management
```bash
# Start new project
django-admin startproject project_name

# Start new app within project
python manage.py startapp app_name

# Check Django version
django-admin --version
python manage.py --version
```

### Database Operations
```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Reverse specific migration
python manage.py migrate app_name migration_number

# Reset all migrations for an app
python manage.py migrate app_name zero

# Show SQL for migration
python manage.py sqlmigrate app_name migration_number
```

### Development Server
```bash
# Start development server (default: localhost:8000)
python manage.py runserver

# Start on specific port
python manage.py runserver 8080

# Start on specific IP and port
python manage.py runserver 0.0.0.0:8000
```

### User Management
```bash
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword username
```

### Django Shell & Testing
```bash
# Open Django shell
python manage.py shell

# Run tests
python manage.py test

# Run tests for specific app
python manage.py test app_name

# Run tests with verbosity
python manage.py test --verbosity=2
```

### Static Files & Media
```bash
# Collect static files for production
python manage.py collectstatic

# Find static files
python manage.py findstatic filename.css
```

### Database Utilities
```bash
# Open database shell
python manage.py dbshell

# Load data from fixture
python manage.py loaddata fixture_name.json

# Create fixture from data
python manage.py dumpdata app_name.ModelName > fixture.json

# Flush database (delete all data)
python manage.py flush
```

### Debugging & Inspection
```bash
# Check for common problems
python manage.py check

# Show detailed system check
python manage.py check --deploy

# Show installed apps and versions
python manage.py diffsettings

# Validate models
python manage.py validate
```

### Custom Management Commands
```bash
# Clear sessions
python manage.py clearsessions

# Clear cache
python manage.py clear_cache

# Send test email
python manage.py sendtestemail email@example.com
```

## Project Structure After Creation
```
myproject/
├── myproject/
│   ├── __init__.py
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI application
│   └── asgi.py          # ASGI application
├── manage.py            # Command-line utility
└── db.sqlite3           # Database (after first migration)
```

## Important Files to Configure

### settings.py
Key settings to review and modify:
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Add your domain names
- `DATABASES`: Configure your database
- `STATIC_URL` and `STATIC_ROOT`: For static files
- `MEDIA_URL` and `MEDIA_ROOT`: For user uploads

### urls.py
Configure URL patterns for your project and apps.

### models.py
Define your database models in each app.

### views.py
Create view functions or classes to handle requests.

### templates/
Create HTML templates for rendering responses.

## Best Practices

1. **Always use virtual environments** to isolate project dependencies
2. **Run migrations** after creating or modifying models
3. **Create superuser** for admin access during development
4. **Use version control** (Git) from the start of your project
5. **Keep settings secure** - use environment variables for sensitive data
6. **Regular testing** with `python manage.py test`
7. **Check for issues** regularly with `python manage.py check`

## Quick Start Checklist

- [ ] Create and activate virtual environment
- [ ] Install Django
- [ ] Create new project with `django-admin startproject`
- [ ] Navigate to project directory
- [ ] Run `python manage.py migrate`
- [ ] Create superuser with `python manage.py createsuperuser`
- [ ] Start development server with `python manage.py runserver`
- [ ] Visit http://127.0.0.1:8000 to see your Django project
- [ ] Visit http://127.0.0.1:8000/admin to access admin panel

## Useful Development Workflow

1. Create new app: `python manage.py startapp myapp`
2. Add app to `INSTALLED_APPS` in settings.py
3. Create models in `models.py`
4. Make migrations: `python manage.py makemigrations`
5. Apply migrations: `python manage.py migrate`
6. Create views in `views.py`
7. Configure URLs in `urls.py`
8. Create templates
9. Test your changes: `python manage.py test`
10. Run development server: `python manage.py runserver`
