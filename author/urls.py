from django.urls import path, include
from .views import *
from rest_framework import routers


urlpatterns = [
    path('', authors, name='authors'),
    path('<int:authorid>/', author_books),
    path('add_author/', add_author, name='add_author'),
    path('delete_author/<int:authorid>/', delete_author, name='delete_author'),

]
