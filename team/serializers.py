from rest_framework.serializers import ModelSerializer

from team.models import Teams


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'