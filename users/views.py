from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Protect Views with Permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsModerator, IsUser

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome, Admin!"})

class ModeratorOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsModerator]

    def get(self, request):
        return Response({"message": "Welcome, Moderator!"})

class UserOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsUser]

    def get(self, request):
        return Response({"message": "Welcome, User!"})


# Role Update Functionality for Admin
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes

@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_role(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        role = request.data.get('role')
        if role in ['admin', 'moderator', 'user']:
            user.role = role
            user.save()
            return Response({'message': 'Role updated successfully!'})
        return Response({'error': 'Invalid role!'}, status=400)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found!'}, status=404)
