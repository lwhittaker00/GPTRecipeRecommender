from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    tools = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def request(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Recipes(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    tools = models.TextField()
    recommendation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_ingredients_list(self):
        import json
        return json.loads(self.ingredients)

    def get_tools_list(self):
        import json
        return json.loads(self.tools)
