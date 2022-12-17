
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenVerifyView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from versionedTodo.v3.router import api_urlpatterns as api_v3
from versionedTodo.v4.router import api_urlpatterns as api_v4


schema_view = get_schema_view(
   openapi.Info(
      title="Todo + Payments Silabuz",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),   
    path('', include('users.urls_apitoken')), 
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include('payment.urls')),
    path('users/', include('users.urls')),
    re_path(r'^api/v3/', include(api_v3)),
    re_path(r'^api/v4/', include(api_v4)),
]



# path('', include('todo.urls')),    
   
# path('api/', include('todo.urls')),

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTMzNzczMiwiaWF0IjoxNjcxMjUxMzMyLCJqdGkiOiIxMjczZTYzNTMxYjk0YWJhOWIxNDQzYjU2MTA4YmJmZCIsInVzZXJfaWQiOjF9.2yxDyu7rITGzsUu3qAIiGCer1HNDr0ORK6HLZRSxmLE",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMjUxNjMyLCJpYXQiOjE2NzEyNTEzMzIsImp0aSI6IjBmZTVjNzMzZWVlZjQyODJhMTBlYjA3MDExODI5MzBmIiwidXNlcl9pZCI6MX0.6hnh8V-OzT5ezcaYwas1fPIPPR2YC5E1tyW-y6iJ3hs"
# }