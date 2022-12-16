from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


from .serializers import SignUpSerializer, GetUserSerializer
from .tokens import create_jwt_pair_for_user
from .models import Users



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


class LoginView(APIView):
    def post(self, request:Request):
        print('POST BABY')
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)

            response = {"message":"Logueado Coorectamente", "username":username, "tokens":tokens}  
            return Response(data = response, status= status.HTTP_200_OK)
        return Response(data={"message":"Invalid Username or incorrect password"})
    
    def get(self, request:Request):
        content = {"user":str(request.user), "auth":str(request.auth)}
        return Response(data=content, status = status.HTTP_200_OK)



class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = Users.objects.all()

