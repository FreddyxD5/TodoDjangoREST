from . import api
from rest_framework import routers
from versionedTodo.v4.api import TodoV4ViewSet, TodoViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet, 'todosCustom')

api_urlpatterns = router.urls

