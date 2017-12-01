from rest_framework import routers, serializers, viewsets

from lab2.models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'age', 'address', 'friends')


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
