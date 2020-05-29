from graphene_django.types import DjangoObjectType
import graphene
from main.models import Task
from django.contrib.auth import User

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ('id', 'assigned_to', 'title', 'description', 'status', 'created_on')

    name = graphene.String()
 
    def resolve_name(self, info, **kwargs):
 	    return 'ACM-BitsPilani-Blog'

    title = graphene.String() 
 
    def resolve_title(self, info, **kwargs):
       return 'Constant-hardcoded Title'
        
    class UserType(DjangoObjectType):
        class Meta:
            model = User
    