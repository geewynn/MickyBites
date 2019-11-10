from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from rest_framework import permissions


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_blank=False, required=True, max_length=200)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=200, allow_blank=True)

    class Meta:

        model = Product
        fields = ['id', 'name', 'price', 'description']


class UserSerializer(serializers.ModelSerializer):
    #product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email']