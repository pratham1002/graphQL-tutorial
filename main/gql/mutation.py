import graphene
from main.gql.typeDef import TaskType
from django.contrib.auth.models import User
from main.models import Task
from django.contrib.auth import User

class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required = True)
        description = graphene.String(required = True)
    
        #Id of user who is creating the task.
        userId = graphene.Int(required = True)
    
        #Define the type of field task variable can hold.
    task = graphene.Field(TaskType)
  
    def mutate(self, info, **kwargs):
        title = kwargs["title"]
        description = kwargs["description"]
        id = kwargs["userId"]

        user = User.objects.get(pk=id)
    
        task = Task.objects.create(title=title, description=description, assigned_to=user)
    
        return CreateTaskMutation(task=task)
    
class Mutation:
 	  create_task = CreateTaskMutation.Field()