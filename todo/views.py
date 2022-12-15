from django.shortcuts import render, get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Todo
from .pagination import StandarResultsSetPagination
from .serializers import TodoSerializer, TestTodoSerializer
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class  = TestTodoSerializer
    pagination_class = StandarResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    search_fields = ['title','body', 'created_at']
    filterset_fields = ('title','body', 'created_at',)


    def create(self, request):
        print('???')
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            print('valido')
            self.perform_create(serializer)
            return Response({'mensaje':'se ha creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response({'error':'ha ocurrido un error'},status=status.HTTP_400_BAD_REQUEST)

    

# class TestTodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     permissions_classes = [permissions.AllowAny]
#     serializer_class  = TestTodoSerializer


# class GetAllTodo(APIView):
#     def get(self, request):
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)



# class AllTodo(APIView):
#     def get(self, request):
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)


class TodoViewSetCustom(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    pagination_class = StandarResultsSetPagination

    def get_serializer_class(self):
        return TodoSerializer
    

    def list(self, request):        
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)       
        return Response({'error':'Aún no hay datos para mostrar.'}, status = status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        print(request.data)
        if isinstance(request.data, list):
            print('lista ')
            serializer = TodoSerializer(data=request.data, many=True)
        else:
            serializer = TodoSerializer(data=request.data)
        
        if serializer.is_valid():
            print('es valido')
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        if todo:
            print('siu')
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        return Response({'error':'Aún no hay datos para mostrar.'}, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk = pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

