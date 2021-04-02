from django.contrib import admin
from django.urls import path, include
from home import views
admin.site.site_header = "Geek Admin"
admin.site.site_title = "Geek Admin Portal"
admin.site.index_title = "Welcome to Geek Admin"

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("page", views.page, name="page")
]