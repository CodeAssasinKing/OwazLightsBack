from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from core.tasks import send_custom_email
from .models import UserCredentials, FeedBack
from django.utils.translation import gettext_lazy as _
from django.conf import settings


@api_view(['POST'])
@permission_classes([AllowAny])
def post_user_credential(request):
    data = request.data
    full_name = data.get('full_name')
    email = data.get('email')

    try:
        user = UserCredentials.objects.create(
            full_name = full_name,
            email = email
        )

        user.save()
        send_custom_email.delay(
            [email], str(_("Welcome to our website AlyX")), str(_("Thank you for staying with us!"))
        )

        return Response({'message': 'User Credential Created'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return Response({'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])
def post_feedback(request):
    data = request.data
    full_name = data.get('full_name')
    email = data.get('email')
    message = data.get('message')

    try:
        FeedBack.objects.create(
            full_name = full_name,
            email = email,
            message = message
        )

        send_custom_email.delay(
            [settings.EMAIL_HOST_USER],
            str("Новое письмо"),
            str(message),
        )
        return Response({'message': 'Feedback Created'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)