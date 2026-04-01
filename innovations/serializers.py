from rest_framework.serializers import ModelSerializer
from innovations.models import Innovations
from products.serializers import ProductsSerializer

class InnovationsSerializer(ModelSerializer):
    products = ProductsSerializer(many=True)
    class Meta:
        model = Innovations
        fields = [
            "id",
            "name",
            "description",
            "image",
            "products",
            "product_description_image",
            "date"
        ]


