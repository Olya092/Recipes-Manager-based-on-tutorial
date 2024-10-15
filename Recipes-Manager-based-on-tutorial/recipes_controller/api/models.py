from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    servings = models.IntegerField()
    temperature  = models.IntegerField()
    cooking_time  = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


