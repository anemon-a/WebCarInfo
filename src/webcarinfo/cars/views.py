from rest_framework import generics
from .models import Car, Comment
from .serializers import CarSerializer, CommentSerializer


class CarAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CommentAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
