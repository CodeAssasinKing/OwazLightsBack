from core.views import StandardPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from products.models import Products, ProductCategory
from products.serializers import ProductsSerializer
from rest_framework import status


class ProductsListView(ListAPIView):
    queryset = Products.objects.select_related("category", 'size').prefetch_related("gallery", "innovations", "video", "news").all().order_by("-date")
    serializer_class = ProductsSerializer
    pagination_class = StandardPagination



@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_categories(request):
    categories = ProductCategory.objects.all()
    serializer = ProductsSerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK )