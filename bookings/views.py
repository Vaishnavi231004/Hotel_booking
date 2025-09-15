from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser
# Create your views here.
from rest_framework import viewsets
from .models import User, Hotel, Room, Booking, Review
from .serializers import UserSerializer, HotelSerializer, RoomSerializer, BookingSerializer, ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':  # POST /api/users/ → signup
            return [AllowAny()]
        return [IsAdminUser()] 

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    from rest_framework.exceptions import PermissionDenied

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'traveler':
            raise PermissionDenied("Only travelers can book rooms.")
        serializer.save(traveler=user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
