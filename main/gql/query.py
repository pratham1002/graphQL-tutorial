import graphene
from .typeDef import TaskType
from main.models import Task

class Query:
    all_tasks = graphene.List(TaskType)

    def resolve_all_tasks(self, info, **kwargs):
  	    return Task.objects.all()