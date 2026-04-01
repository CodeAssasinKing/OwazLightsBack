from rest_framework.serializers import ModelSerializer, SerializerMethodField
from news.models import Category, Gallery, News
from products.serializer import ProductsSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'



class NewsSerializer(ModelSerializer):
    category = SerializerMethodField('category.name')
    gallery = GallerySerializer(many=True)
    products = ProductsSerializer(many=True)
    class Meta:
        model = News
        fields = [
            "id",
            "category",
            "gallery",
            "title",
            "short_description",
            "content",
            "date",
            "products"
        ]


