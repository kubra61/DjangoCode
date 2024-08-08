from django.urls import path()
from .views import *

urlpatterns=[
    path("",index)
    path("anasayfa/",index),
    path("books/",books)
]