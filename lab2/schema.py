from graphene import Node, ObjectType, Schema
from graphene_django import DjangoConnectionField, DjangoObjectType

from lab2.models import Profile


class ProfileNode(DjangoObjectType):
    class Meta:
        model = Profile
        interfaces = (Node,)


class Query(ObjectType):
    profile = Node.Field(ProfileNode)
    all_profiles = DjangoConnectionField(ProfileNode)


schema = Schema(query=Query)
