from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def function_view(request):
    return HttpResponse('response from function view')

class ExampleClassBased(View):
    def get(selfself, request):
        return HttpResponse('response from class based view')

class ExampleView(View):
    def get(self, request):
        return render(request, 'myfile.html', {'dict': {'inner': 'a'}})

class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', data)