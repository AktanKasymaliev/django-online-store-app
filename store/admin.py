from django.contrib import admin
from .models import Category, Product, LaptopsCategory, SmartPhonesCategory
from django import forms
from django.forms import ValidationError
from PIL import Image


# Настройка изображения
class AdminForm(forms.ModelForm):
    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте картинку не меньше {}x{}'.format(*self.MIN_RESOLUTION)

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Загруженное изображение не соответствует минимальным требованиям')
        return image


# Настройка выбора категории в админ панеле
class LaptopAdmin(admin.ModelAdmin):
    form = AdminForm

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(Category.objects.filter(name__icontains='ноутбуки'))
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class SmartPhoneAdmin(admin.ModelAdmin):
    form = AdminForm

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(Category.objects.filter(name__icontains='смартфоны'))
        return super().formfield_for_dbfield(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(LaptopsCategory, LaptopAdmin)
admin.site.register(SmartPhonesCategory, SmartPhoneAdmin)
