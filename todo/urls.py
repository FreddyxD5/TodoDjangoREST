from rest_framework import routers

from .views import TodoViewSet,TodoViewSetCustom

urlpatterns = []

router = routers.DefaultRouter()

router.register('v1/todo', TodoViewSet, basename='todo')
router.register('v3/todo', TodoViewSetCustom, basename='todoCustom')
# router.register('v2/todoall', AllTodo, basename='fullView')

urlpatterns = router.urls
