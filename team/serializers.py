from rest_framework.serializers import ModelSerializer

from team.models import Teams, OurValues


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class ValueSerializer(ModelSerializer):
    class Meta:
        model = OurValues
        fields = '__all__'