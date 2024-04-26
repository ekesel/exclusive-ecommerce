from .views import *
from django.urls import path, include


urlpatterns = [
    path('homepageconfigs', homepageconfigs, name="homepageconfigs"),
    path("login_configs", login_configs, name="login_configs"),
    path('register', register, name='register'),
    path('login', login, name='login'),
]