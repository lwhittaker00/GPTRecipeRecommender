from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    tools = models.TextField()
    recommendation = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_ingredients_list(self):
        import json
        return json.loads(self.ingredients)

    def get_tools_list(self):
        import json
        return json.loads(self.tools)
