from core.views import StandardPagination
from news.models import News, Category
from rest_framework.generics import ListAPIView
from news.serializers import (
    NewsSerializer,
    CategorySerializer,
    NewsSerializerWithRelatedNews,
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class NewsListView(ListAPIView):
    def get_queryset(self):
        queryset = (
            News.objects.select_related("category")
            .prefetch_related("gallery", "products")
            .order_by("-date")
        )
        category_id = self.request.query_params.get("category", None)
        if category_id:
            category = Category.objects.get(id=category_id)
            queryset = queryset.filter(category=category)
        return queryset

    serializer_class = NewsSerializer
    pagination_class = StandardPagination


@api_view(["GET"])
@permission_classes([AllowAny])
def get_three_news(request):
    news = News.objects.all().order_by("-date")[:6]
    serializer = NewsSerializer(news, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_news_category(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_exact_news(request, id):
    news = News.objects.get(id=id)
    serializer = NewsSerializerWithRelatedNews(news, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
