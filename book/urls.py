from django.urls import path, include
from .views import *
from rest_framework import routers


#router = routers.SimpleRouter()
#router.register(r'book', BookViewSet)

urlpatterns = [
    path('', books, name='books'),
    path('sorted/', books_sorted_by_names, name='books_sorted_by_names'),
    path('sorted_desc/', books_sorted_by_names_desc,
         name='books_sorted_by_names_desc'),
    path('sorted_count/', books_sorted_by_count, name='books_sorted_by_count'),
    path('<int:bookid>/', book_by),
    path('add_book/', add_book, name='add_book'),
    path('update_book/<str:bookid>/', update_book, name='update_book'),
    path('del_book/<str:bookid>/', del_book, name='del_book'),
   # path('api/v1/', include(router.urls)),
]


