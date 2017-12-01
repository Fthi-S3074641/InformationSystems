import graphene
from graphene_django import DjangoObjectType

from lab2.models import Profile


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Query(graphene.ObjectType):
    profile = graphene.Field(ProfileType,
                             id=graphene.Int(),
                             name=graphene.String()
                             )
    all_profiles = graphene.List(ProfileType)

    def resolve_all_profiles(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_profile(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Profile.objects.get(pk=id)

        if name is not None:
            return Profile.objects.get(name=name)

        return None


schema = graphene.Schema(query=Query)
