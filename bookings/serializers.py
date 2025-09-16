from rest_framework import serializers
from .models import User, Hotel, Room, Booking, Review

from rest_framework import serializers
from .models import User

from rest_framework import serializers
from .models import User, Hotel, Room, Booking, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'read_only': True}  # frontend cannot set role
        }

    def create(self, validated_data):
        # enforce traveler role for all frontend signups
        validated_data['role'] = 'traveler'
        user = User.objects.create_user(**validated_data)  # ✅ create_user hashes password
        return user


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
