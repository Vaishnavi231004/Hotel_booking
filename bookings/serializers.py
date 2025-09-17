from rest_framework import serializers
from .models import User, Hotel, Room, Booking, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'read_only': True}  
        }

    def create(self, validated_data):
        validated_data['role'] = 'traveler'
        user = User.objects.create_user(**validated_data)  
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
        read_only_fields = ['traveler'] 

class ReviewSerializer(serializers.ModelSerializer):
    traveler = serializers.ReadOnlyField(source='traveler.username') 

    class Meta:
        model = Review
        fields = '__all__'
