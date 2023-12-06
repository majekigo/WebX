from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def catalog(request):
    return render(request, 'catalog.html')


def product_detail(request, product_id):
    return render(request, 'product_detail.html', {'product_id': product_id})


def product_add(request):
    return HttpResponse("Добавление товара")


def product_edit(request, product_id):
    return HttpResponse(f"Редактирование товара {product_id}")


def product_delete(request, product_id):
    return HttpResponse(f"Удаление товара {product_id}")


def user_profile(request):
    return render(request, 'user_profile.html')


def cart(request):
    return render(request, 'cart.html')


def feedback(request):
    return render(request, 'feedback.html')
