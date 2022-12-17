from rest_framework import viewsets
from payment.models  import Payment, Service
from payment.serializers import PaymentSerializer, ServiceSerializer
from rest_framework.permissions import IsAuthenticated


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes=[IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes=[IsAuthenticated] 
