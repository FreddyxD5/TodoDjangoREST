from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import action



class TodoV4ViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'body']
    ordering = ('-id')
    throttle_classes = [UserRateThrottle]

    #Detail = True, es una vista de detalle (Retrieve, update, get)
    @action(detail=True, methods=["post"], throttle_classes=[UserRateThrottle])
    def example_adhoc_method(self, request, pk=None):        
        content = {
            'status':'request was permitted'
        }        
        return Response(content)
   


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'body']
    ordering = ('-id')

    # Definición de la clave
    throttle_scope = 'get'

    