from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    tools = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    requested_date = models.DateTimeField(blank=True, null=True)

    def request(self):
        self.requested_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
