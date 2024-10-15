from rest_framework import serializers
from .models import Recipe

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'servings', 'temperature', 'cooking_time', 'ingredients', 'instructions', 'created_at')