from core.views import StandardPagination
from news.models import News, Category, Gallery
from rest_framework.generics import ListAPIView
from news.serializers import NewsSerializer, CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class NewsListView(ListAPIView):
    queryset = News.objects.select_related("category").prefetch_related("gallery", "products").order_by("-date")
    serializer_class = NewsSerializer
    pagination_class = StandardPagination



@api_view(['GET'])
@permission_classes([AllowAny])
def get_news_category(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)