import graphene
from main.gql.query import Query as MainQuery
from main.gql.mutation import Mutation as MainMutation


class Mutation(MainMutation, graphene.ObjectType):
     pass

class Query(MainQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)