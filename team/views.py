from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from team.models import Teams
from team.serializers import TeamSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_team(request):
    queryset = Teams.objects.all().order_by("-date")
    serialized_data = TeamSerializer(queryset, many=True, context={'request': request})
    return Response(serialized_data.data, status=status.HTTP_200_OK)
