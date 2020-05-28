from graphene_django.types import DjangoObjectType
from main.models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ('id', 'assigned_to', 'title', 'description', 'status', 'created_on')