from django.urls import path
from .views import RegisterView, LoginView
from .views import AdminOnlyView, ModeratorOnlyView, UserOnlyView
from .views import update_role

urlpatterns = [
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('moderator-only/', ModeratorOnlyView.as_view(), name='moderator-only'),
    path('user-only/', UserOnlyView.as_view(), name='user-only'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update-role/<int:user_id>/', update_role, name='update-role'),
]
