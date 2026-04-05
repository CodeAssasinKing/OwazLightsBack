from core.views import StandardPagination
from rest_framework.generics import ListAPIView
from videos.serializers import VideosSerializer
from videos.models import Videos


class VideoListView(ListAPIView):
    queryset = Videos.objects.all().order_by("-date")
    serializer_class = VideosSerializer
    pagination_class = StandardPagination
