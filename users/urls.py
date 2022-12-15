from rest_framework import routers
from .api import  UserViewSetOne, UserMixinViewSet, UserViewSet
from django.urls import path
from users.routers import CustomRouter

router = CustomRouter()

# router.register('', UserViewSet, basename = 'users')
router.register('', UserMixinViewSet, basename = 'users')
# router.register('', UserViewSetOne, basename='oneUser')

urlpatterns = router.urls