"""
Django settings for exclusive project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from collections import OrderedDict


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h_hj_4vpdy#syg2n9tlqa(=!93)12ee3u(h=i6b8+5gddeqqe!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'constance',
    'constance.backends.database',
    'rest_framework.authtoken',
    'corsheaders',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'exclusive.urls'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
  'http://localhost:3000',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'exclusive.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# django-constance config

CONSTANCE_SUPERUSER_ONLY = False
CONSTANCE_BACKEND = 'constance.backends.memory.MemoryBackend'

CONSTANCE_ADDITIONAL_FIELDS = {
    'json_field': ['exclusive.constance_add_fields.ConstanceJSONField', {}],
}

CONSTANCE_CONFIG = OrderedDict([
    # (key_name, (default_value, helptext, field_type)),
    ('TOP_BANNER', ({
    "text":"Summer Sale For All Swim Suits And Free Express Delivery - OFF 50%!",
    "link":"http://google.com"
    }, 'This is a top exclusive offer banner, please use dict format only', 'json_field')),
    ('SITE_TITLE', ('Exclusive', 'This is site name', str)),
    ('IMAGE_BANNER', ({
        "link":"http://google.com",
        "image_link":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2m99wWgQ-wpPFmSuxgicyuBDgbt9IUb4izw&usqp=CAU"
    }, 'This is a list of image banners', 'json_field')),
    ('FLASH_SALE', ({
    "1":{
        "start_date":"12/03/2024",
        "end_date":"13/04/2024",
        "start_time":"02:08:00",
        "end_time":"10:07:00"
    }
    }, 'Give Flash Deal product ids here', 'json_field')),
    ('CATEGORY_BANNER', ({
    "background_image_link":"http://www.google.com",
    "start_date":"12/03/2024",
    "end_date":"13/04/2024",
    "start_time":"02:08:00",
    "end_time":"10:07:00",
    "product_link":"http://www.google.com"
    }, 'This is category banner', 'json_field')),
    ('NEW_ARRIVAL_BANNER_1', ({
    "background_image_link":"https://images.unsplash.com/photo-1607853202273-797f1c22a38e?q=80&w=1854&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "product_link":"http://www.google.com"
    }, 'This is new arrival banner 1', 'json_field')),
    ('NEW_ARRIVAL_BANNER_2', ({
    "background_image_link":"https://plus.unsplash.com/premium_photo-1664908364593-729f67b1a0e4?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8d29tZW4lMjBjb2xsZWN0aW9ufGVufDB8fDB8fHww",
    "product_link":"http://www.google.com"
    }, 'This is new arrival banner 2', 'json_field')),
    ('NEW_ARRIVAL_BANNER_3', ({
    "background_image_link":"https://images.unsplash.com/photo-1517756548657-b2c24162e63d?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "product_link":"http://www.google.com"
    }, 'This is new arrival banner 3', 'json_field')),
    ('NEW_ARRIVAL_BANNER_4', ({
    "background_image_link":"https://plus.unsplash.com/premium_photo-1670445044667-3c24bd5330b4?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "product_link":"http://www.google.com"
    }, 'This is new arrival banner 4', 'json_field')),
    ('MOTIVE_1', ({
    "icon_link":"http://www.google.com",
    "title":"FREE AND FAST DELIVERY",
    "desc":"Free delivery for all orders over $140"
    }, 'This is motive 1', 'json_field')),
    ('MOTIVE_2', ({
    "icon_link":"http://www.google.com",
    "title":"24/7 CUSTOMER SERVICE",
    "desc":"Friendly 24/7 customer support"
    }, 'This is motive 2', 'json_field')),
    ('MOTIVE_3', ({
        'icon_link': 'http://www.google.com',
        'title': 'MONEY BACK GUARANTEE',
        'desc': 'We return money within 30 days',
    }, 'This is motive 3', 'json_field')),
    ('INSTAGRAM_LINK', ('http://instagram.com', 'This is instagram link', str)),
    ('X_LINK', ('http://x.com', 'This is x link', str)),
    ('FACEBOOK_LINK', ('http://fb.com', 'This is facebook link', str)),
    ('LINKEDIN_LINK', ('http://linkedin.com', 'This is linkedin link', str)),
    ('APP_DETAILS', ({
        'playstore_link': 'http://www.google.com',
        'appstore_link': 'http://www.google.com',
    }, 'This contains app details', 'json_field')),
    ('ADDRESS', ('111 Bijoy sarani, Dhaka,  DH 1515, Bangladesh.', 'Enter store address here', str)),
    ('EMAIL', ('exclusive@gmail.com', 'Enter email here', str)),
    ('PHONE', ('+88015-88888-9999', 'Enter phone number here', str)),
    ('ABOUT_TITLE', ('Our Story', 'Enter About us title here', str)),
    ('ABOUT_DESC_1', ('Launced in 2015, Exclusive is South Asia’s premier online shopping makterplace with an active presense in Bangladesh. Supported by wide range of tailored marketing, data and service solutions, Exclusive has 10,500 sallers and 300 brands and serves 3 millioons customers across the region.', 'Enter About us description first para here', str)),
    ('ABOUT_DESC_2', ('Exclusive has more than 1 Million products to offer, growing at a very fast. Exclusive offers a diverse assotment in categories ranging  from consumer.', 'Enter About us description second para here', str)),
    ('ABOUT_US_IMAGE', ('http://google.com', 'enter about us image here', str)),
    ('ACHIEVEMENT_1', ({
    "icon_link":"http://www.google.com",
    "title":"45.5k",
    "desc":"Customer active in our site"
    }, 'This is achievement 1', 'json_field')),
    ('ACHIEVEMENT_2', ({
    "icon_link":"http://www.google.com",
    "title":"10.5k",
    "desc":"Sallers active our site"
    }, 'This is achievement 2', 'json_field')),
    ('ACHIEVEMENT_3', ({
    "icon_link":"http://www.google.com",
    "title":"33k",
    "desc":"Monthly Produduct Sale"
    }, 'This is achievement 3', 'json_field')),
    ('ACHIEVEMENT_4', ({
    "icon_link":"http://www.google.com",
    "title":"25k",
    "desc":"Annual gross sale in our site"
    }, 'This is achievement 4', 'json_field')),
    ('EMPLOYEES', ("[{ 'name': 'Tom Cruise', 'role': 'Managing Director' ,'insta_link': 'http://google.com', 'image_link': 'http://google.com', 'fb_link': 'http://google.com', 'x_link': 'http://google.com' }]", 'This is a list of employees on about us page', str)),
    ('CALL_US_TITLE', ('Call To Us', 'This is call to us title in contact page', str)),
    ('CALL_US_ICON', ('http://google.com', 'This is call to us icon link in contact page', str)),
    ('CALL_US_DESC', ('We are available 24/7, 7 days a week.', 'This is call to us description in contact page', str)), 
    ('CALL_US_PHONE', ('Phone: +8801611112222', 'This is call to us phone number in contact page', str)),
    ('EMAIL_US_TITLE', ('Write To US', 'This is email to us title in contact page', str)),
    ('EMAIL_US_DESC', ('Fill out our form and we will contact you within 24 hours.', 'This is email to us description in contact page', str)),
    ('EMAIL_US_ICON', ('http://google.com', 'This is write to us icon link in contact page', str)),
    ('EMAIL_US_EMAILS', ('Emails: customer@exclusive.com', 'This is email to us emails in contact page', str)),
])

CONSTANCE_CONFIG_FIELDSETS = {
    'BANNERS': ('TOP_BANNER', 'IMAGE_BANNER', 'CATEGORY_BANNER', 'NEW_ARRIVAL_BANNER_1', 'NEW_ARRIVAL_BANNER_2',
                'NEW_ARRIVAL_BANNER_3', 'NEW_ARRIVAL_BANNER_4', ),
    'SITE_DETAILS': ('SITE_TITLE', ),
    'SALE': ('FLASH_SALE', ),
    'MOTIVES': ('MOTIVE_1', 'MOTIVE_2', 'MOTIVE_3', ),
    'SOCIAL_LINKS': ('LINKEDIN_LINK', 'FACEBOOK_LINK', 'X_LINK', 'INSTAGRAM_LINK', ),
    'APP_DETAILS': ('APP_DETAILS', ),
    'SUPPORT_DETAILS': ('ADDRESS', 'EMAIL', 'PHONE', ),
    'ABOUT_US': ('ABOUT_TITLE', 'ABOUT_DESC_1', 'ABOUT_DESC_2', 'ABOUT_US_IMAGE', 'ACHIEVEMENT_1', 'ACHIEVEMENT_2',
                 'ACHIEVEMENT_3', 'ACHIEVEMENT_4', 'EMPLOYEES', ),
    'CONTACT_US': ('CALL_US_TITLE', 'CALL_US_DESC', 'CALL_US_PHONE', 'CALL_US_ICON', 'EMAIL_US_TITLE',
                   'EMAIL_US_DESC', 'EMAIL_US_ICON', 'EMAIL_US_EMAILS', ),
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}