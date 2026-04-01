from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from innovations.models import Innovations
from innovations.serializers import InnovationsSerializer
from core.views import StandardPagination



class InnovationsListView(ListAPIView):
    queryset = Innovations.objects.prefetch_related("products").order_by("-date")
    serializer_class = InnovationsSerializer
    pagination_class = StandardPagination