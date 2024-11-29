from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly

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


import requests
import logging
# Set up logging
logger = logging.getLogger(__name__)

class UpdateRoleView(APIView):
    # Permission classes to ensure only authenticated users can access this view
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    def patch(self, request, user_id):
        try:
            # The user making the request
            requesting_user = request.user  
            
            # Ensure the user is authenticated and has the proper role
            if requesting_user.role != 'admin':
                return Response({'error': 'You do not have permission to update roles.'}, status=status.HTTP_403_FORBIDDEN)

            # Prevent users from modifying their own roles
            if requesting_user.id == user_id:
                return Response({'error': 'You cannot modify your own role.'}, status=status.HTTP_403_FORBIDDEN)

            # Try to get the target user by user_id
            target_user = CustomUser.objects.get(id=user_id)
            
            # Extract the role from the request data
            role = request.data.get('role')

            # Validate the role
            if role not in ['admin', 'moderator', 'user']:
                return Response({'error': 'Invalid role!'}, status=status.HTTP_400_BAD_REQUEST)

            # Log the role update action
            logger.info(f"User {requesting_user.id} updated role of User {user_id} to {role}")
            
            # Update the role of the target user
            target_user.role = role
            target_user.save()

            return Response({'message': 'Role updated successfully!'}, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)



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
