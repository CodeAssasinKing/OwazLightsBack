from django.urls import path
from applications.views import post_application
from user_creditentals.views import post_user_credential

app_name = 'core'


urlpatterns = [
    # applications
    path("post-application", post_application),
#     user_creditenalts
    path("post-user-credential", post_user_credential),
]