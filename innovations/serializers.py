from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from innovations.models import Innovations

class InnovationsSerializer(ModelSerializer):
    products = SerializerMethodField()

    def get_products(self, obj):
        items = obj.products.all().order_by("-date")[:10]
        request = self.context.get("request")
        serialized_data = [
            {
                "id": item.id,
                "poster": request.build_absolute_uri(item.poster.url),
                "name": item.name,
            }
        for item in items]
        return serialized_data

    class Meta:
        model = Innovations
        fields = [
            "id",
            "name",
            "description",
            "image",
            "product_description_image",
            "date",
            "products"
        ]


