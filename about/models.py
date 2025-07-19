from django.db import models

# Create your models here.


# Stores information from contact form
class Contact(models.Model):
    """
    Stores information from contact form
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    sent_on = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
