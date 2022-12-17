from rest_framework import routers
from payment.api import ServiceViewSet, PaymentViewSet

router = routers.DefaultRouter()
router.register('services', ServiceViewSet, basename='services')
router.register('payment', PaymentViewSet, basename='payment')
urlpatterns = router.urls