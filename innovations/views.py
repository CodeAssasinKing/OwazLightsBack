from rest_framework import response, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from innovations.models import Innovations
from innovations.serializers import InnovationsSerializer
from core.views import StandardPagination



class InnovationsListView(ListAPIView):
    queryset = Innovations.objects.prefetch_related("products").order_by("-date")
    serializer_class = InnovationsSerializer
    pagination_class = StandardPagination


@api_view(["GET"])
@permission_classes([AllowAny])
def get_exact_innovation(request, id):
    innovations = Innovations.objects.get(id=id)
    serializer = InnovationsSerializer(innovations, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)