from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Textbook, Order
from .serializers import TextbookSerializer, OrderSerializer

class TextbookListView(APIView):
    def get(self, request):
        textbooks = Textbook.objects.all()
        serializer = TextbookSerializer(textbooks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TextbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TextbookDetailView(APIView):
    def get_object(self, pk):
        try:
            return Textbook.objects.get(pk=pk)
        except Textbook.DoesNotExist:
            return None

    def get(self, request, pk):
        textbook = self.get_object(pk)
        if textbook is not None:
            serializer = TextbookSerializer(textbook)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
        
class TextbookImageView(APIView): 
    def get(self, request, pk): 
        textbook = Textbook.objects.get(pk=pk) 
        image = textbook.image 
        return Response({'image': image.url})
    
