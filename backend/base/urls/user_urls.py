from django.urls import path
from ..views import user_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('login/', user_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('profile/', user_views.getUserProfile, name="user"),
    path('profile/update/', user_views.updateUserProfile, name="user-profile"),
    path('register/', user_views.registerUser, name="register"),
    path('', user_views.getUsers, name="users"),
]
