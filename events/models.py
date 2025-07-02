from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    max_capacity = models.IntegerField()
    cost = models.FloatField()
    publish_on = models.DateTimeField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
