from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, CategoryForm, TagForm
from .models import Product, Category, Tag


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

#Новые вьюхи


def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})


def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_add.html', {'form': form})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    products = Product.objects.filter(tags=tag)
    return render(request, 'tag_detail.html', {'tag': tag, 'products': products})


def tag_add(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'tag_add.html', {'form': form})

