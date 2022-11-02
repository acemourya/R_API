from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def update(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def destroy(self, request, pk=None):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
