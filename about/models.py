from django.db import models

# Create your models here.


class Contact(models.Model):
    """
    Stores informatio from contact form
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    sent_on = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
