from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from team.models import Teams, OurValues
from team.serializers import TeamSerializer, ValueSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_team(request):
    queryset = Teams.objects.all().order_by("-date")
    our_values = OurValues.objects.all()
    serialized_data = TeamSerializer(queryset, many=True, context={'request': request})
    values_serialized = ValueSerializer(our_values, many=True, context={'request': request})
    return Response({"teams": serialized_data.data, "values": values_serialized.data}, status=status.HTTP_200_OK)
