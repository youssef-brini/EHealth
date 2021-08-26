import graphene
import users.schema
import aboutPatient.schema

class Query(users.schema.Query,aboutPatient.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation,aboutPatient.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)