from django.contrib import admin
from django.urls import path
from myapp import views

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signupview, name='signup'),
    path('login', views.loginview, name='login'),
    path('next', views.Next, name='next'),
]
