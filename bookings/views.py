from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets

from .models import User, Hotel, Room, Booking, Review
from .serializers import UserSerializer, HotelSerializer, RoomSerializer, BookingSerializer, ReviewSerializer


from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({
            "id": user.id,
            "username": user.username,
            "role": getattr(user, "role", "traveler")  # default role
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':  # Anyone can signup
            return [AllowAny()]
        return [IsAdminUser()]  # Only admins can view/manage users


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # Admin can see all bookings
            return Booking.objects.all()
        return Booking.objects.filter(traveler=user)  # Travelers only see their own bookings

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'traveler':
            raise PermissionDenied("Only travelers can book rooms.")
        serializer.save(traveler=user)



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
