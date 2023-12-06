from django.urls import path

from api.views import get_products, get_product, create_product, update_product, delete_product

urlpatterns = [
    path('', get_products),
    path('<int:product_id>/', get_product),
    path('create/', create_product),
    path('<int:product_id>/update/', update_product),
    path('<int:product_id>/delete/', delete_product),
]