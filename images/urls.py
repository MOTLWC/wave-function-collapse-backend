from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import ImageCreateIndex, ImageGetByUserId, ImageGetDelete

urlpatterns = [
    path("", ImageCreateIndex.as_view()),
    path("get-by-user/<int:userId>/", ImageGetByUserId.as_view()),
    path("<int:imageId>/", ImageGetDelete.as_view()),
]