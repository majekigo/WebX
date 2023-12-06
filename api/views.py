from django.http import HttpResponse

# Create your views here.


def get_products(request):
    return HttpResponse("Получить все товары")


def get_product(request, product_id):
    return HttpResponse(f"Получить товар {product_id}")


def create_product(request):
    return HttpResponse("Создать новый товар")


def update_product(request, product_id):
    return HttpResponse(f"Обновить товар {product_id}")


def delete_product(request, product_id):
    return HttpResponse(f"Удалить товар {product_id}")