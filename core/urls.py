from django.urls import path
from applications.views import post_application
from core.views import get_banners
from innovations.views import InnovationsListView, get_exact_innovation
from news.views import NewsListView, get_news_category, get_three_news, get_exact_news
from products.views import ProductsListView, get_product_categories
from team.views import get_team
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
    path("innovations/<int:id>", get_exact_innovation),
#     news
    path("news", NewsListView.as_view()),
    path("get-news-categories", get_news_category),
    path("main-news", get_three_news),
    path("get-exact-news/<int:id>", get_exact_news),
#     products
    path("products", ProductsListView.as_view()),
    path("get-product-categories", get_product_categories),
#     videos
    path("videos", VideoListView.as_view()),
#     team
    path("get-teams", get_team)
]