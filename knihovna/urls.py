from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('books/', views.book_list_view, name='book_list'),
    path('authors/', views.author_list_view, name='author_list'),
    path('books/<int:id>/', views.book_id_view, name='book_detail_view'),
    path('authors/<int:id>/', views.author_id_view, name='author_detail_view'),
    path('borrowed/', views.book_borrowed_view, name='book_borrowed'),
    path('search/', views.book_search_view, name='search_results'),
]
