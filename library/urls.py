"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from authentication.views import UserViewSet
from author.views import AuthorViewSet
from book.views import BookViewSet
from order.views import OrderViewSet

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'order', OrderViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', include('author.urls')),
    path('orders/', include('order.urls')),
    path('users/', include('authentication.urls')),
    path('book/', include('book.urls')),
    path('', include('book.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/user/<int:user_id>/order/<int:order_id>/', OrderViewSet.as_view({'get': 'specific'}), name='user_specific'),
]
