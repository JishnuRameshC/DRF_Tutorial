from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookAPIListView.as_view(), name='book_list'),
]