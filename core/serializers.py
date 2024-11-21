from rest_framework import serializers
from .models import CustomUser, Trip

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'full_name', 'bio', 'profile_image', 'is_premium']

class TripSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    friends = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'user', 'friends']
