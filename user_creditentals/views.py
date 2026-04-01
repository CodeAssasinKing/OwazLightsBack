from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import UserCredentials



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

        return Response({'message': 'User Credential Created'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)