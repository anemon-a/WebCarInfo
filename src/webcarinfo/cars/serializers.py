from rest_framework import serializers
from .models import Car, Comment


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = ["make", "model", "year", "description", "owner"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # car = serializers.HiddenField(default=)

    class Meta:
        model = Comment
        fields = "__all__"
