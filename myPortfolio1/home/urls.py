from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin customization
admin.site.site_header = "Login To Robert Kamau AdminPort"
admin.site.site_title = "Welcome to Developer Robert's AdminPort"
admin.site.index_title = "Welcome Kiongozi"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
]