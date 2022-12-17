from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


from .serializers import SignUpSerializer, GetUserSerializer, LoginSerializer
from .tokens import create_jwt_pair_for_user
from .models import Users

from drf_yasg.utils import swagger_auto_schema


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request:Request):
        data = request.data

        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()            
            response = {"message":"Usuario creado correctamente", "data":serializer.data}
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    # @swagger_auto_schema(operation_description="Login de Usuario que retorna un token"        
    # )
    def post(self, request:Request):        
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)

            response = {"message":"Logueado Coorectamente", "username":username, "tokens":tokens}  
            return Response(data = response, status= status.HTTP_200_OK)
        return Response(data={"message":"Invalid Username or incorrect password"})
    
    # @swagger_auto_schema(operation_description="Retorna el usuario xd?"        
    # )
    def get(self, request:Request):
        content = {"user":str(request.user), "auth":str(request.auth)}
        return Response(data=content, status = status.HTTP_200_OK)



class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = Users.objects.all()

