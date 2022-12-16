from django.db import models
from users.models import Users
# Create your models here.
class Todo(models.Model):
    authors = models.ForeignKey(Users, on_delete=models.CASCADE, related_name = 'todos', null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    done_at = models.DateField(null=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'