from django import forms
from django.core.exceptions import ValidationError

from .models import Product, Category, Tag


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'tags']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 1:
            raise ValidationError("Цена должна быть больше 0.")
        return price

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise ValidationError("Имя должно содержать не менее 3 символов.")
        if not name.isalnum():
            raise ValidationError("Имя может содержать только буквы и цифры.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise ValidationError("Описание должно содержать не менее 10 символов.")
        if len(description) > 150:
            raise ValidationError("Описание не может содержать более 15 символов.")
        if '😊' in description or '😄' in description:
            raise ValidationError("Использование смайликов запрещено.")
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.content_type == 'image/gif':
                raise ValidationError("Загрузка GIF изображений недопустима.")
        return image


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise ValidationError("Название категории должно содержать не менее 2 символов.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 5:
            raise ValidationError("Описание категории должно содержать не менее 5 символов.")
        return description


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name[0].isalpha():
            raise ValidationError("Имя тега должно начинаться с буквы.")
        return name
