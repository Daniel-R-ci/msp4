from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles")
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    publish_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
