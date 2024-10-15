from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import generics
from .serializers import RecipesSerializer
from .models import Recipe

# Create your views here.
# def main(request):
#     return HttpResponse("Hello")


class RecipeView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

