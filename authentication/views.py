from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from order.models import Order
from .models import CustomUser
from .forms import *
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


    @action(methods=['get'], detail=True)
    def orders(self, request, pk=None):
        orders = Order.objects.filter(user=pk)
        return Response({'orders_id':[order.pk for order in orders]})


def users(request):
    context = {
        'users': CustomUser.objects.all(),
    }
    return render(request, 'users.html', context=context)


def add_user(request):
    if request.method == 'POST':
        form = AddUserPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = AddUserPostForm()
    return render(request, 'add_user.html', {'form': form})


def delete_user(request, userid):
    print('DELETE')
    user = CustomUser.objects.get(pk=userid)
    user.delete()
    return redirect('users')
