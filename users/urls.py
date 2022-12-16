from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path
from users.routers import CustomRouter
# from .api import  UserViewSetOne, UserMixinViewSet, UserViewSet
from . import views


# router = CustomRouter()
# # router.register('', UserViewSet, basename = 'users')
# router.register('', UserMixinViewSet, basename = 'users')
# # router.register('', UserViewSetOne, basename='oneUser')



router = routers.DefaultRouter()
router.register('', views.GetUsers, basename='obtener_usuarios')

urlpatterns=[
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify')
]



urlpatterns += router.urls