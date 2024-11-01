from books.models import Book
from rest_framework import generics
from .serializer import BookSerializer
# Create your views here.


class BookAPIListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer