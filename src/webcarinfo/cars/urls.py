from django.urls import path

from .views import *

urlpatterns = [
    path("cars/", CarListAPIView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailAPIView.as_view(), name="car-detail"),
    path("cars/<int:pk>/comments/",
         CommentListAPIView.as_view(), name="comments-list"),
]
