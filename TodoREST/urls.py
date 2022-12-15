
from django.contrib import admin
from django.urls import path, include, re_path

from versionedTodo.v3.router import api_urlpatterns as api_v3
from versionedTodo.v3.router import api_urlpatterns as api_v4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    # path('api/', include('todo.urls')),
    path('users/', include('users.urls')),
    re_path(r'^api/v3/', include(api_v3)),
    re_path(r'^api/v4/', include(api_v4)),
]
