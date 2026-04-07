from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField
import os
from innovations.serializers import InnovationsSerializer
from news.serializers import NewsSerializer
from products.models import ProductSize, ProductCategory, ProductGallery, ProductDocumentations, Products, \
    ProductSubcategory
from videos.serializers import VideosSerializer


class ProductSizeSerializer(ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSubcategorySerializer(ModelSerializer):
    category = CharField(source='category.name', read_only=True)
    category_id = CharField(source='category.id', read_only=True)
    class Meta:
        model = ProductSubcategory
        fields = [
            "id",
            "name",
            "category",
            "category_id",
            "poster"
        ]

class ProductGallerySerializer(ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = '__all__'

class ProductDocumentationsSerializer(ModelSerializer):
    file_url = SerializerMethodField()
    file_extension = SerializerMethodField()
    original_filename = SerializerMethodField()

    def get_file_url(self, obj):
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None

    def get_file_extension(self, obj):
        if obj.file:
            return os.path.splitext(obj.file.name)[1].lower()
        return None

    def get_original_filename(self, obj):
        if obj.file:
            return os.path.basename(obj.file.name)
        return None

    class Meta:
        model = ProductDocumentations
        fields = ['id', 'name', 'file_url', 'file_extension', 'original_filename',
                  'description', 'file_size', 'created_at', 'is_active']
        read_only_fields = ['created_at', 'file_size']


class ProductsSerializer(ModelSerializer):
    category = CharField(source='category.name', read_only=True)
    subcategory = CharField(source='subcategory.name', read_only=True)
    category_id = CharField(source='category.id', read_only=True)
    subcategory_id = CharField(source='subcategory.id', read_only=True)
    size = CharField(source='size.name', read_only=True)
    gallery = ProductGallerySerializer(many=True)
    innovations = InnovationsSerializer(many=True)
    video = VideosSerializer(many=True)
    news = SerializerMethodField()
    product_documentations = ProductDocumentationsSerializer(many=True)
    def get_news(self, obj):
        query_set = obj.news.all().order_by('-date')[:6]
        request = self.context.get('request')
        serialized_date = NewsSerializer(query_set, many=True, context={"request": request}).data
        return serialized_date
    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "poster",
            "short_description",
            "description",
            "category",
            "subcategory",
            "category_id",
            "subcategory_id",
            "size",
            "gallery",
            "innovations",
            "video",
            "news",
            "date",
            "product_documentations"
        ]

