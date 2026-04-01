from django.urls import path
from applications.views import post_application
from core.views import get_banners
from user_creditentals.views import post_user_credential

app_name = 'core'


urlpatterns = [
    # applications
    path("post-application", post_application),
#     user_creditenalts
    path("post-user-credential", post_user_credential),
#     banners
    path("get-banners", get_banners)
]