from rest_framework.serializers import ModelSerializer
from innovations.models import Innovations

class InnovationsSerializer(ModelSerializer):
    def get_fields(self):
        fields = super().get_fields()
        from products.serializers import ProductsSerializer # Импорт внутри!
        fields['products'] = ProductsSerializer(many=True, read_only=True)
        return fields

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


