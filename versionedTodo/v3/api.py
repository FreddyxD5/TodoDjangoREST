from todo.models import Todo
from rest_framework import viewsets
from .serializers import TodoV3Serializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters


class TodoViewSetCustom(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        return TodoV3Serializer

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        print('siiuuu')
        print(page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = TodoV3Serializer(request.data, many=True)
        else:
            serializer = TodoV3Serializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
         todo = get_object_or_404(self.queryset, pk=pk)
         serializer = TodoV3Serializer(todo)
         return Response(serializer.data)

    def update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = TodoV3Serializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = TodoV3Serializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)