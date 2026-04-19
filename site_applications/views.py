from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from site_applications.models import Application
from site_applications.serializers import ApplicationSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
@permission_classes([AllowAny])
def get_application(request):
    applications = Application.objects.all().order_by("priority")
    serializer = ApplicationSerializer(applications, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["GET"])
@permission_classes([AllowAny])
def get_exact_application(request, id):
    applications = Application.objects.get(id=id)
    serializer = ApplicationSerializer(applications, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)