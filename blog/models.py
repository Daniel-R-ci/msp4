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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def number_of_comments(self):
        return Article_Comment.objects.filter(
            article=self, visible=True).count()


class Article_Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='article_commenter')
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} commenting on {self.article} on {self.posted_on}"
