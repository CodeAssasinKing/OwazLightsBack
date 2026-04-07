from django.db.models import Model
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from news.models import Category, Gallery, News


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'



class NewsSerializer(ModelSerializer):
    category = CharField(source='category.name', read_only=True)
    category_id = CharField(source='category.id', read_only=True)
    gallery = GallerySerializer(many=True)

    class Meta:
        model = News
        fields = [
            "id",
            "category",
            "category_id",
            "gallery",
            "title",
            "short_description",
            "content",
            "date",
            'poster'
        ]




class NewsSerializerWithRelatedNews(ModelSerializer):
    category = CharField(source='category.name', read_only=True)
    category_id = CharField(source='category.id', read_only=True)
    gallery = GallerySerializer(many=True)
    related_news = SerializerMethodField()
    products = SerializerMethodField()

    def get_products(self, obj):
        items = obj.products.all().order_by("-date")[:10]
        request = self.context.get("request")
        serialized_data = [
            {
                "id": item.id,
                "poster": request.build_absolute_uri(item.poster.url),
                "name": item.name,
                "category": item.category.name,
            }
        for item in items]
        return serialized_data


    def get_related_news(self, obj):
        items = News.objects.filter(category=obj.category).exclude(id=obj.id).order_by("-date")[:4]
        return NewsSerializer(items, many=True, context=self.context).data


    class Meta:
        model = News
        fields = [
            "id",
            "category",
            "category_id",
            "gallery",
            "title",
            "short_description",
            "content",
            "date",
            'poster',
            "related_news",
            "products"
        ]


