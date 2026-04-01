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
    category = SerializerMethodField('category.name')
    gallery = GallerySerializer(many=True)

    def get_fields(self):
        fields = super().get_fields()
        from products.serializers import ProductsSerializer
        fields['products'] = ProductsSerializer(many=True, read_only=True)
        return fields

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


