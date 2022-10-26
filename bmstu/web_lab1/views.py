from django.shortcuts import render
from datetime import date

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return render(request, 'index.html', { 'data' : {'current_date': date.today()}})
def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Витамин А (100 табл)', 'id': 1},
            {'title': 'Комплекс витаминов группы  В (100 капс)', 'id': 2},
            {'title': 'Витамин С 500 мг', 'id': 3},

        ]
    }})
def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})