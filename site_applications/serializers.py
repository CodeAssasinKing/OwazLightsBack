from rest_framework.serializers import ModelSerializer
from site_applications.models import Application
from news.serializers import NewsSerializer


class ApplicationSerializer(ModelSerializer):
    related_news = NewsSerializer(many=True, read_only=True)

    class Meta:
        model = Application
        fields = [
            "id",
            "title",
            "description",
            "poster",
            "date",
            "priority",
            "related_news",
        ]
