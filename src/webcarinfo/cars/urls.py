from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'api/cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/cars/<int:pk>/comments/',
         CommentViewSet.as_view(), name='comment-list-create'),
    path('cars/', car_list, name='car_list'),
    path('cars/add/', car_create, name='car_create'),
    path('cars/<int:pk>/edit/', car_update, name='car_update'),
    path('cars/<int:pk>/delete/', car_delete, name='car_delete'),
    path('cars/<int:pk>/', car_detail, name='car_detail'),
    path('cars/<int:pk>/comments/add/', add_comment, name='add_comment'),
]
