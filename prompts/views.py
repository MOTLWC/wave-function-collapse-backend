from rest_framework.views import APIView
from rest_framework.response import Response 
from utility.handle_exceptions import handle_exceptions
from .models import Prompt
from .serializers.common import PromptSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utility.ownerPermissions import IsOwnerOrReadOnly

class PromptCreateIndex(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly, ]

    @handle_exceptions
    def get(self, request):
        prompts = Prompt.objects.all()
        serialized_prompts = PromptSerializer(prompts, many=True)
        return Response(serialized_prompts.data)
    
    @handle_exceptions
    def post(self, request):
        prompt_to_create = PromptSerializer(data=request.data)
        if prompt_to_create.is_valid():
            prompt_to_create.save()
            return Response(prompt_to_create.data, 201)
        print(f"Invalid Data : {prompt_to_create.errors}")
        return Response(prompt_to_create.errors, 400)
    
class PromptGetByUserId(APIView):

    permission_classes = [IsOwnerOrReadOnly, ]

    @handle_exceptions
    def get(self, request, userId):
        prompt = Prompt.objects.filter(createdBy = userId)
        serialized_prompt = PromptSerializer(prompt, many=True)
        return Response(serialized_prompt.data)
    
class PromptGetDelete(APIView):
    
    permission_classes = [IsOwnerOrReadOnly,]

    @handle_exceptions
    def get(self, request, promptId):
        prompt = Prompt.objects.get(pk = promptId)
        serialized_prompt = PromptSerializer(prompt)
        return Response(serialized_prompt.data)

    @handle_exceptions
    def delete(self, request, promptId):
        prompt_to_delete = Prompt.objects.get(pk=promptId)
        prompt_to_delete.delete()
        return Response(f"All fields at ID: {promptId} deleted", 200)
    
    @handle_exceptions
    def put(self, request, promptId):
        prompt = Prompt.objects.get(pk=promptId)
        serializer = PromptSerializer(prompt, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,200)
        return Response(serializer.errors, 400)
        