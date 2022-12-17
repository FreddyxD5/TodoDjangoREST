from rest_framework import serializers
from todo.models import Todo

class TodoV4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = 'created_at', 'done_at', 'updated_at', 'deleted_at'