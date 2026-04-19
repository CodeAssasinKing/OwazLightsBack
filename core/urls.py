from django.urls import path
from applications.views import post_application
from core.views import get_banners
from innovations.views import InnovationsListView, get_exact_innovation
from news.views import NewsListView, get_news_category, get_three_news, get_exact_news
from products.views import (
    ProductsListView,
    get_product_categories,
    get_product_subcategories,
    get_exact_product,
    get_sizes,
    files_list_view,
    get_file_detail,
    download_file,
    get_popular_products,
)
from site_applications.views import get_application, get_exact_application
from team.views import get_team
from user_creditentals.views import post_user_credential, post_feedback
from videos.views import VideoListView

app_name = "core"


urlpatterns = [
    # applications
    path("post-application", post_application),
    #     user_creditenalts
    path("post-user-credential", post_user_credential),
    path("post-feedback", post_feedback),
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
    path("get-popular-products/", get_popular_products),
    path("get-product-subcategories/<int:id>", get_product_subcategories),
    path("get-product/<int:id>", get_exact_product),
    path("sizes", get_sizes),
    path("get-files/", files_list_view, name="get-files"),
    path("get-files/<int:id>/", get_file_detail, name="get-file-detail"),
    path("download-file/<int:id>/", download_file, name="download-file"),
    #     videos
    path("videos", VideoListView.as_view()),
    #     team
    path("get-teams", get_team),
#     applications
    path("get-applications", get_application),
    path("get-applications/<int:id>", get_exact_application),
]
