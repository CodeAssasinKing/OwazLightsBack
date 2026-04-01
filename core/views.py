from rest_framework.permissions import AllowAny
from core.models import Banners
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from core.serializer import BannerSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_banners(request):
    banners = Banners.objects.all().order_by('-priority')
    serialized_banners = BannerSerializer(banners, many=True)
    return Response(serialized_banners.data, status=status.HTTP_200_OK)
