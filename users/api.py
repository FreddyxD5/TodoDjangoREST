from .models import Users
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from todo.pagination import StandarResultsSetPagination

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    # lookup_field = 'username'

    # def get(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)
        
    def list(self, request):
        print('what')
        serializer = self.serializer_class(self.queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    def create(self, request, pk=None):
        return Response({'message':'CREACION DE ITEM  exito'}, status = status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        return Response({'message':'Actualizado Parcial UPDATE con exito'}, status = status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response({'message':'Retrieve view'}, status = status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        return Response({'message':'Actualizado PUT con exito'}, status = status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        return Response({'message':'borrado Ac exito'}, status =  status.HTTP_200_OK)


class UserMixinViewSet(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    pagination_class = StandarResultsSetPagination


    def list(self, request, *args, **kwargs):
        print('UserMixinViewSet-- LIST')
        return super().list(request, *args, **kwargs)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
            # return Response({'message':'siuuu'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)

    


class UserViewSetOne(
    RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    lookup_field = "username"

    def retrieve(self, request, *args, **kwargs):
        print('UserMixinViewsEToNE-- RETRIEVE')
        return super().retrieve(request, *args, **kwargs)

    