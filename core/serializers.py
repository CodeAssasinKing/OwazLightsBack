from rest_framework import serializers
from core.models import Banners


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = [
            "id",
            "title",
            "banner_image",
            "short_description",
            "url",
            "date"
        ]
