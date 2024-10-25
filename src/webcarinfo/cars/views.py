from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly

from .models import Car, Comment
from .serializers import CarSerializer, CommentSerializer


class CarListAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(car=1)  # как сделать
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )
