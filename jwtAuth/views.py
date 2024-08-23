from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import UserSerializer

class SignUpView(APIView):
    def post(self, request):
        newUser = UserSerializer(data = request.data)
        if newUser.is_valid():
            newUser.save()
            return Response({"message":"Success"})
        print(newUser)
        return Response(newUser.errors)