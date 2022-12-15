from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
            "created_at",
            "done_at",
            "updated_at",
            "deleted_at",
            "status",
        )

        read_only_fields = ('created_at', 'done_at', 'updated_at','deleted_at', )

class TestTodoSerializer(serializers.Serializer):
    id = serializers.IntegerField()    
    title = serializers.CharField(max_length=100)
    body = serializers.CharField()
    created_at = serializers.DateField()

    def validate_title(self, value):
        if "$" in value:
            raise serializers.ValidationError("Error, el titulo no puede tener el simbolo de $")
        return value

    
    def validate_body(self, value):
        if "$" in value:
            raise serializers.ValidationError("Error, el cuerpo no puede tener el simbolo $")
        return value




class TodoTaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    status = serializers.IntegerField()

    def validate_title(self, value):
        if value is None or value =="":
            raise serializers.ValidationError("El campo no puede estar vacío.")

    def validate_body(self, value):
        if value is None or value =="":
            raise serializers.ValidationError("Este campo no puede estar vacío.")
        

