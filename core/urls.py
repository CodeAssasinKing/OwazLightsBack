from django.urls import path
from applications.views import post_application
from core.views import get_banners
from innovations.views import InnovationsListView
from news.views import NewsListView, get_news_category
from products.views import ProductsListView, get_product_categories
from user_creditentals.views import post_user_credential
from videos.views import VideoListView

app_name = 'core'


urlpatterns = [
    # applications
    path("post-application", post_application),
#     user_creditenalts
    path("post-user-credential", post_user_credential),
#     banners
    path("get-banners", get_banners),
#     innovations
    path("innovations", InnovationsListView.as_view()),
#     news
    path("news", NewsListView.as_view()),
    path("get-news-categories", get_news_category),
#     products
    path("products", ProductsListView.as_view()),
    path("get-product-categories", get_product_categories),
#     videos
    path("videos", VideoListView.as_view()),
]