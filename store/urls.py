from django.urls import path

from store.views import home, catalog, product_detail, product_add, product_edit, product_delete, feedback, \
    user_profile, cart, index

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
]