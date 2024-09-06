from rest_framework.views import APIView
from rest_framework.response import Response 
from utility.handle_exceptions import handle_exceptions
from .models import Image
from .serializers.common import ImageSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utility.ownerPermissions import IsOwnerOrReadOnly

class ImageCreateIndex(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly, ]

    @handle_exceptions
    def get(self, request):
        images = Image.objects.all()
        serialized_images = ImageSerializer(images, many=True)
        return Response(serialized_images.data)

    @handle_exceptions
    def post(self, request):
        image_to_create = ImageSerializer(data=request.data)
        if image_to_create.is_valid():
            image_to_create.save()
            return Response(image_to_create.data, 201)
        print(f"Invalid Data : {image_to_create.errors}")
        return Response(image_to_create.errors, 400)

class ImageGetByUserId(APIView):
    
    permission_classes = [IsOwnerOrReadOnly, ]

    @handle_exceptions
    def get(self, request, userId):
        image = Image.objects.filter(createdBy = userId)
        serialized_image = ImageSerializer(image, many=True)
        return Response(serialized_image.data)

class ImageGetDelete(APIView):

    permission_classes = [IsOwnerOrReadOnly,]

    @handle_exceptions
    def get(self, request, imageId):
        image = Image.objects.get(pk = imageId)
        serialized_image = ImageSerializer(image)
        return Response(serialized_image.data)

    @handle_exceptions
    def delete(self, request, imageId):
        image_to_delete = Image.objects.get(pk=imageId)
        image_to_delete.delete()
        return Response(f"All fields at ID: {imageId} deleted", 200)

    