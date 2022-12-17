from rest_framework import viewsets
from django_filters import rest_framework as filters
from payment.models  import Payment, Service
from payment.serializers import PaymentSerializer, ServiceSerializer
from rest_framework.permissions import IsAuthenticated
from todo.pagination import StandarResultsSetPagination


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    permission_classes=[IsAuthenticated]
    pagination_class = StandarResultsSetPagination
    throttle_scope = 'services'

    class Meta:
        ordering = ['-id']

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all().order_by('id')
    permission_classes=[IsAuthenticated] 
    pagination_class = StandarResultsSetPagination

    filter_backends = [filters.DjangoFilterBackend]    
    filterset_fields = ('user__id','payment_date', 'service',)

    throttle_scope = 'payments'
    class Meta:
        ordering = ['-id']
