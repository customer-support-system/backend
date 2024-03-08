from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ComplaintViewSet, LevelViewSet,
    SolutionViewSet, StaffViewSet, CustomUserViewSet,CustomTokenObtainPairView
)
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet, basename='complaint')
router.register(r'levels', LevelViewSet, basename='level')
router.register(r'solutions', SolutionViewSet, basename='solution')
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'users', CustomUserViewSet)


urlpatterns = [
    path('login/',    CustomTokenObtainPairView.as_view(), name='login'),
    path('token/',    CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
