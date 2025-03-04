from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import SaveSerializer, ReceiveSerializer

@api_view(['POST'])
def snippet_create(request):
    if request.method == 'POST':
        serializer = SaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def receive_user_data(request):
    if request.method == 'POST':
        serializer = ReceiveSerializer(data=request.data)
        if serializer.is_valid():
            # داده‌های اعتبارسنجی شده در اینجا پردازش می‌شوند
            validated_data = serializer.validated_data
            return Response(validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Users.objects.all()
        serializer = SaveSerializer(snippets, many=True)
        return Response(serializer.data)

