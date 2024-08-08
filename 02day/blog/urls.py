from django.urls import path
from .views import index, about

urlpatterns = [
    path("", index),
    path("about/", about)
]

# http://127.0.0.1:8000/blog/about