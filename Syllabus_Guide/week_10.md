# Django Web Development Course - Week 10: Deployment & Production

## Course Description
This course provides a comprehensive introduction to Django, a high-level Python web framework that enables rapid development of secure and maintainable websites. Students will learn to build dynamic web applications from scratch using Django's powerful components and best practices.

## Module 1: Preparing for Production

### Production Settings Configuration

```python
# settings/production.py
"""
Production settings for Django project.
"""
import os
from .base import *
import dj_database_url
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'yourdomain.com',
    'www.yourdomain.com',
    'your-app.herokuapp.com',
    '127.0.0.1',  # For local testing
]

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', 587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', 'noreply@yourdomain.com')

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'myapp': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_URL', 'redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Session configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Static files storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Django REST Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    }
}
```

### Environment Configuration

```python
# settings/base.py
"""
Base settings for Django project.
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'corsheaders',
    'storages',
    
    # Local apps
    'myapp',
    'users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
    "https://www.yourdomain.com",
]

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'
```

```bash
# .env file (for local development)
# Copy this to .env.production for production
SECRET_KEY=your-super-secret-production-key-here
DEBUG=False
DATABASE_URL=postgres://username:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379/0
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Module 2: Git and Source Control Management

### Git Configuration and Workflow

```bash
# .gitignore for Django projects
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Django stuff
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/
staticfiles/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Deployment
.docker/
compose.yml
docker-compose*
```

```bash
# Git setup and basic commands

# Initialize git repository
git init

# Configure git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main

# Basic workflow
git status                    # Check status
git add .                     # Add all files
git add specific_file.py      # Add specific file
git commit -m "Initial commit" # Commit changes
git log                       # View commit history

# Branching strategy
git branch                    # List branches
git branch feature-branch     # Create new branch
git checkout feature-branch   # Switch to branch
git checkout -b feature-branch # Create and switch to branch

# Merging
git checkout main
git merge feature-branch      # Merge feature branch into main

# Remote repositories
git remote add origin https://github.com/username/repository.git
git push -u origin main       # First push
git push origin feature-branch # Push branch to remote

# Tagging for releases
git tag v1.0.0               # Create tag
git push origin v1.0.0        # Push tag to remote
```

### Git Workflow for Django Projects

```bash
# Complete deployment workflow example

# 1. Create feature branch
git checkout -b feature/user-authentication

# 2. Make changes and commit
git add .
git commit -m "Add user authentication with login, logout, and registration"

# 3. Push to remote
git push origin feature/user-authentication

# 4. Create Pull Request on GitHub/GitLab

# 5. After PR approval, merge to develop
git checkout develop
git merge feature/user-authentication

# 6. Test on staging

# 7. Prepare release
git checkout main
git merge develop
git tag v1.1.0
git push origin main --tags

# 8. Deploy to production
```

```yaml
# .github/workflows/django.yml
# GitHub Actions for CI/CD
name: Django CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.8, 3.9, 3.10]

    services:
      postgres:
        image: postgres:13
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: github_actions
        ports:
          - 5432:5432
        options: --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5

    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
        
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install coverage
        
    - name: Run Tests
      env:
        DATABASE_URL: postgres://postgres:postgres@localhost:5432/github_actions
        SECRET_KEY: test-secret-key
      run: |
        python manage.py test --noinput
        coverage run manage.py test
        coverage report
        
    - name: Security Check
      run: |
        pip install safety
        safety check
        
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to Production
      run: |
        echo "Deploying to production..."
        # Add your deployment commands here
```

## Module 3: Deploying Django Project

### Deployment to Heroku

```yaml
# runtime.txt
python-3.10.8

# requirements.txt
Django==4.2.4
gunicorn==21.2.0
whitenoise==6.5.0
psycopg2-binary==2.9.6
dj-database-url==2.0.0
python-decouple==3.8
django-cors-headers==4.2.0
django-storages==1.13.2
boto3==1.28.4
Pillow==10.0.0
celery==5.3.1
redis==4.5.5
django-redis==5.2.0
```

```python
# Procfile
web: gunicorn myproject.wsgi --log-file -
worker: celery -A myproject worker --loglevel=info
beat: celery -A myproject beat --loglevel=info

# Or for multiple processes:
# web: gunicorn myproject.wsgi --workers 3 --threads 2 --log-file -
# release: python manage.py migrate
```

```python
# myproject/wsgi.py (Production ready)
"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.production')

application = get_wsgi_application()

# For WhiteNoise static file serving
from whitenoise import WhiteNoise
application = WhiteNoise(application, root='staticfiles')
application.add_files('static', prefix='static/')
application.add_files('media', prefix='media/')
```

### Deployment to AWS Elastic Beanstalk

```yaml
# .ebextensions/django.config
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: myproject.settings.production
  aws:elasticbeanstalk:container:python:
    WSGIPath: myproject.wsgi:application
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: staticfiles

commands:
  01_migrate:
    command: "django-admin migrate"
    leader_only: true
  02_collectstatic:
    command: "django-admin collectstatic --noinput"

container_commands:
  01_syncdb:
    command: "django-admin syncdb --noinput"
    leader_only: true
  02_createsu:
    command: "django-admin createsuperuser --noinput --username admin --email admin@example.com"
    leader_only: true
    ignoreErrors: true

files:
  "/opt/elasticbeanstalk/hooks/appdeploy/pre/01_setup_env.sh":
    mode: "000755"
    owner: root
    group: root
    content: |
      #!/bin/bash
      cd /var/app/current
      source /var/app/venv/staging-lg-1/bin/activate
      python manage.py collectstatic --noinput
```

```python
# .ebextensions/01_packages.config
packages:
  yum:
    postgresql95-devel: []
    gcc: []
    python3-devel: []
```

### Deployment to DigitalOcean App Platform

```yaml
# digitalocean-app.yaml
name: my-django-app
services:
- name: web
  github:
    repo: username/my-django-app
    branch: main
  run_command: gunicorn --worker-tmp-dir /dev/shm myproject.wsgi:application
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  routes:
  - path: /
  source_dir: /
  http_port: 8000

databases:
- name: db
  engine: PG
  version: "13"
  size_slug: db-s-1vcpu-1gb
  num_nodes: 1

envs:
- key: DJANGO_SETTINGS_MODULE
  value: myproject.settings.production
- key: SECRET_KEY
  value: ${SECRET_KEY}
- key: DEBUG
  value: "False"
- key: DATABASE_URL
  value: ${db.DATABASE_URL}
```

### Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=myproject.settings.production

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
        musl-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Create non-root user
RUN useradd -m -U appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "myproject.wsgi:application"]
```

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  web:
    build: 
      context: .
      dockerfile: Dockerfile
    command: gunicorn --bind 0.0.0.0:8000 --workers 3 myproject.wsgi:application
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    expose:
      - 8000
    env_file:
      - .env.production
    depends_on:
      - db
      - redis
    networks:
      - django_network

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    env_file:
      - .env.production
    networks:
      - django_network

  redis:
    image: redis:6-alpine
    volumes:
      - redis_data:/data
    networks:
      - django_network

  nginx:
    image: nginx:1.21-alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - web
    networks:
      - django_network

  celery:
    build: 
      context: .
      dockerfile: Dockerfile
    command: celery -A myproject worker --loglevel=info
    volumes:
      - .:/app
    env_file:
      - .env.production
    depends_on:
      - db
      - redis
    networks:
      - django_network

  celery-beat:
    build: 
      context: .
      dockerfile: Dockerfile
    command: celery -A myproject beat --loglevel=info
    volumes:
      - .:/app
    env_file:
      - .env.production
    depends_on:
      - db
      - redis
    networks:
      - django_network

volumes:
  postgres_data:
  redis_data:
  static_volume:
  media_volume:

networks:
  django_network:
    driver: bridge
```

```nginx
# nginx/nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream django {
        server web:8000;
    }

    server {
        listen 80;
        server_name yourdomain.com www.yourdomain.com;
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name yourdomain.com www.yourdomain.com;

        ssl_certificate /etc/nginx/ssl/cert.pem;
        ssl_certificate_key /etc/nginx/ssl/key.pem;

        # Security headers
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-XSS-Protection "1; mode=block" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header Referrer-Policy "no-referrer-when-downgrade" always;
        add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

        location / {
            proxy_pass http://django;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
        }

        location /static/ {
            alias /app/staticfiles/;
            expires 1y;
            add_header Cache-Control "public, immutable";
        }

        location /media/ {
            alias /app/media/;
            expires 1y;
            add_header Cache-Control "public, immutable";
        }

        # Security
        location ~ /\. {
            deny all;
        }

        location ~ /\.ht {
            deny all;
        }
    }
}
```

### Deployment Scripts and Automation

```bash
#!/bin/bash
# deploy.sh - Automated deployment script

set -e  # Exit on any error

echo "Starting deployment process..."

# Load environment variables
source .env.production

# Pull latest changes
echo "Pulling latest changes..."
git pull origin main

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Clear cache
echo "Clearing cache..."
python manage.py clear_cache

# Restart application server
echo "Restarting application server..."
sudo systemctl restart gunicorn

# Restart Celery workers
echo "Restarting Celery workers..."
sudo systemctl restart celery
sudo systemctl restart celerybeat

# Run health check
echo "Running health check..."
curl -f http://localhost:8000/health/ || exit 1

echo "Deployment completed successfully!"
```

```python
# management/commands/deploy.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
import subprocess
import sys

class Command(BaseCommand):
    help = 'Automated deployment script'

    def add_arguments(self, parser):
        parser.add_argument(
            '--migrate',
            action='store_true',
            help='Run database migrations',
        )
        parser.add_argument(
            '--collectstatic',
            action='store_true',
            help='Collect static files',
        )
        parser.add_argument(
            '--restart-services',
            action='store_true',
            help='Restart application services',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting deployment...'))

        # Run database migrations
        if options['migrate']:
            self.stdout.write('Running database migrations...')
            try:
                call_command('migrate')
                self.stdout.write(self.style.SUCCESS('Migrations completed'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Migration failed: {e}'))
                sys.exit(1)

        # Collect static files
        if options['collectstatic']:
            self.stdout.write('Collecting static files...')
            try:
                call_command('collectstatic', '--noinput')
                self.stdout.write(self.style.SUCCESS('Static files collected'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Static collection failed: {e}'))
                sys.exit(1)

        # Restart services
        if options['restart_services']:
            self.stdout.write('Restarting services...')
            try:
                subprocess.run(['sudo', 'systemctl', 'restart', 'gunicorn'], check=True)
                subprocess.run(['sudo', 'systemctl', 'restart', 'celery'], check=True)
                self.stdout.write(self.style.SUCCESS('Services restarted'))
            except subprocess.CalledProcessError as e:
                self.stdout.write(self.style.ERROR(f'Service restart failed: {e}'))
                sys.exit(1)

        self.stdout.write(self.style.SUCCESS('Deployment completed successfully!'))
```

### Monitoring and Maintenance

```python
# Monitoring and health checks
from django.http import JsonResponse
from django.views import View
from django.db import connection
from django.core.cache import cache
import redis
import psutil

class HealthCheckView(View):
    def get(self, request):
        checks = {
            'database': self.check_database(),
            'cache': self.check_cache(),
            'storage': self.check_storage(),
            'memory': self.check_memory(),
        }
        
        status = 200 if all(checks.values()) else 503
        return JsonResponse({
            'status': 'healthy' if all(checks.values()) else 'unhealthy',
            'checks': checks
        }, status=status)
    
    def check_database(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            return True
        except:
            return False
    
    def check_cache(self):
        try:
            cache.set('health_check', 'ok', 1)
            return cache.get('health_check') == 'ok'
        except:
            return False
    
    def check_storage(self):
        try:
            # Check if we can write to storage
            with open('health_check.tmp', 'w') as f:
                f.write('test')
            import os
            os.remove('health_check.tmp')
            return True
        except:
            return False
    
    def check_memory(self):
        try:
            # Check if memory usage is reasonable
            memory_usage = psutil.virtual_memory().percent
            return memory_usage < 90  # Alert if memory usage > 90%
        except:
            return False

# Custom middleware for monitoring
import time
from django.utils.deprecation import MiddlewareMixin

class MonitoringMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
    
    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            
            # Log slow requests
            if duration > 2.0:  # 2 seconds
                print(f"Slow request: {request.path} took {duration:.2f}s")
            
            # Add timing header
            response['X-Response-Time'] = f"{duration:.2f}s"
        
        return response
```

### Backup and Recovery

```python
# management/commands/backup.py
from django.core.management.base import BaseCommand
from django.conf import settings
import subprocess
import os
from datetime import datetime
import boto3

class Command(BaseCommand):
    help = 'Backup database and media files'

    def handle(self, *args, **options):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = f'/tmp/backups/{timestamp}'
        
        # Create backup directory
        os.makedirs(backup_dir, exist_ok=True)
        
        # Backup database
        self.stdout.write('Backing up database...')
        db_backup_path = self.backup_database(backup_dir, timestamp)
        
        # Backup media files
        self.stdout.write('Backing up media files...')
        media_backup_path = self.backup_media(backup_dir, timestamp)
        
        # Upload to cloud storage
        if hasattr(settings, 'AWS_STORAGE_BUCKET_NAME'):
            self.stdout.write('Uploading to cloud storage...')
            self.upload_to_s3(backup_dir, timestamp)
        
        self.stdout.write(self.style.SUCCESS('Backup completed successfully!'))

    def backup_database(self, backup_dir, timestamp):
        db_settings = settings.DATABASES['default']
        backup_file = f'{backup_dir}/database_{timestamp}.sql'
        
        if db_settings['ENGINE'] == 'django.db.backends.postgresql':
            cmd = [
                'pg_dump',
                '-h', db_settings.get('HOST', 'localhost'),
                '-U', db_settings['USER'],
                '-d', db_settings['NAME'],
                '-f', backup_file
            ]
            
            # Set password for pg_dump
            env = os.environ.copy()
            env['PGPASSWORD'] = db_settings['PASSWORD']
            
            subprocess.run(cmd, env=env, check=True)
        
        return backup_file

    def backup_media(self, backup_dir, timestamp):
        media_dir = settings.MEDIA_ROOT
        backup_file = f'{backup_dir}/media_{timestamp}.tar.gz'
        
        cmd = ['tar', '-czf', backup_file, '-C', media_dir, '.']
        subprocess.run(cmd, check=True)
        
        return backup_file

    def upload_to_s3(self, backup_dir, timestamp):
        s3 = boto3.client('s3')
        
        for file_name in os.listdir(backup_dir):
            file_path = os.path.join(backup_dir, file_name)
            s3_key = f'backups/{timestamp}/{file_name}'
            
            s3.upload_file(file_path, settings.AWS_STORAGE_BUCKET_NAME, s3_key)
            
            self.stdout.write(f'Uploaded: {s3_key}')
```

This comprehensive Week 10 module covers Django deployment and production readiness, providing students with the knowledge needed to deploy Django applications to various platforms, implement CI/CD pipelines, and maintain production applications with proper monitoring and backup strategies.