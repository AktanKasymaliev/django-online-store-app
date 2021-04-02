from django.urls import path, include
from .views import (RegisterView, activating,
                TokenObtainPairView, UsersView,
                UserUpdateView)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<slug:uidb64>/<slug:token>/', activating, name='activate'),
    path('auth/token/', TokenObtainPairView.as_view(), name='access'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/', include('djoser.urls.authtoken')),
    path('', UsersView.as_view(), name='users'),
    path('upd/<int:pk>/', UserUpdateView.as_view(), name='user_update')
]
