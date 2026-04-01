from rest_framework import serializers
from core.models import Banners


class BannerSerializer(serializers.Serializer):
    class Meta:
        model = Banners
        fields = "__all__"
