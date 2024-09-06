from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PromptCreateIndex, PromptGetByUserId, PromptGetDelete

urlpatterns = [
    path("", PromptCreateIndex.as_view()),
    path("get-by-user/<int:userId>/", PromptGetByUserId.as_view() ),
    path("<int:promptId>/", PromptGetDelete.as_view())
]