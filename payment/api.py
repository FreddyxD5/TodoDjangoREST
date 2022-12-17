from rest_framework import viewsets
from django_filters import rest_framework as filters
from payment.models  import Payment, Service
from payment.serializers import PaymentSerializer, ServiceSerializer
from rest_framework.permissions import IsAuthenticated


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes=[IsAuthenticated]
    throttle_scope = 'services'

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes=[IsAuthenticated] 

    filter_backends = [filters.DjangoFilterBackend]    
    filterset_fields = ('user__id','payment_date', 'service',)

    throttle_scope = 'payments'
