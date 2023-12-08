from django.urls import path
from .views import (
    index, home, catalog, product_detail, product_add, product_edit,
    product_delete, user_profile, cart, feedback, category_list,
    category_detail, category_add, tag_list, tag_detail, tag_add
)

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('product/add/', product_add, name='product_add'),
    path('product/<int:product_id>/edit/', product_edit, name='product_edit'),
    path('product/<int:product_id>/delete/', product_delete, name='product_delete'),
    path('profile/', user_profile, name='profile'),
    path('cart/', cart, name='cart'),
    path('feedback/', feedback, name='feedback'),

    path('categories/', category_list, name='category_list'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('category/add/', category_add, name='category_add'),

    path('tags/', tag_list, name='tag_list'),
    path('tag/<int:tag_id>/', tag_detail, name='tag_detail'),
    path('tag/add/', tag_add, name='tag_add'),
]
