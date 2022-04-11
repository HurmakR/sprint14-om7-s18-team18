from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Order, Book
from book.models import Book
from .forms import *
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def orders(request):
    context = {
        'orders': Order.objects.all(),
        'books': Book.objects.all(),

    }
    return render(request, 'order/orders.html', context)


def order_by(request, orderid):

    context = {
        'order': Order.get_by_id(orderid),
    }
    return render(request, 'order/order.html', context)


def add_order(request):
    if request.method == 'POST':
        form = AddOrderPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = AddOrderPostForm()
    return render(request, 'order/add_order.html', {'form': form})


def update_order(request, orderid):
    print('UPDATE')
    order = Order.objects.get(pk=orderid)
    form = AddOrderPostForm(instance=order)
    if request.method == 'POST':
        print('POST')
        form = AddOrderPostForm(request.POST, instance=order)
        if form.is_valid():
            print('VALID')
            form.save()
            return redirect('orders')
    return render(request, 'order/add_order.html', {'form': form})


def delete_order(request, orderid):
    print('DELETE')
    order = Order.objects.get(pk=orderid)
    order.delete()
    return redirect('orders')
