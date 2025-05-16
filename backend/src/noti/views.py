from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NotiOwner
from .serializers import NotiOwnerSerializer


class NotiOwnerView(APIView):
    def post(self, request):
        serializer = NotiOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
