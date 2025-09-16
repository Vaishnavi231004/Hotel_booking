from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HotelViewSet, RoomViewSet, BookingViewSet, ReviewViewSet, login_view

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
]
