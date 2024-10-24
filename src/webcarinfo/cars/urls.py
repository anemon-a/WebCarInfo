from django.urls import path

from .views import CarAPIView

urlpatterns = [
    path("cars/", CarAPIView.as_view(), name="car-list"),
    # path("articles/<int:pk>/", CarDetail.as_view(), name="car-detail"),
]
