from rest_framework.serializers import ModelSerializer, SerializerMethodField

from innovations.serializer import InnovationsSerializer
from news.serializer import NewsSerializer
from products.models import ProductSize, ProductCategory, ProductGallery, ProductDocumentations, Products
from videos.serializer import VideosSerializer


class ProductSizeSerializer(ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductGallerySerializer(ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = '__all__'


class ProductDocumentationsSerializer(ModelSerializer):
    class Meta:
        model = ProductDocumentations
        fields = '__all__'


class ProductsSerializer(ModelSerializer):
    category = SerializerMethodField('category.name')
    size = SerializerMethodField('size.name')
    gallery = ProductGallerySerializer(many=True)
    innovations = InnovationsSerializer(many=True)
    video = VideosSerializer(many=True)
    news = NewsSerializer(many=True)
    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "poster",
            "short_description",
            "description",
            "category",
            "size",
            "gallery"
            "innovations",
            "video",
            "news",
            "date"
        ]