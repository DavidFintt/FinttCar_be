from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    model = get_user_model
    fields = ['id', 'first_name', 'last_name', 'dealership']

    