from django.db import models
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200) # str Charfield
    content = models.TextField() # str(long) textfield
    pub_date = models.DateTimeField(auto_now_add=True) # time Date/DateTime/DateTimeField
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)  # str charfield
    email = models.EmailField() # str EmailField