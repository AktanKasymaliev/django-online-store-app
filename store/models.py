from django.db import models
from django.contrib.contenttypes.models import ContentType



# Мэнеджеры контекстов
class LatestProductManager:
    @staticmethod
    def get_last_products(*args, **kwargs):
        products = []
        models_ct = ContentType.objects.filter(model__in=args)
        for ct_model in models_ct:
            our_prod = ct_model.model_class()._base_manager.all().order_by('-id')[:6]
            products.extend(our_prod)
        return products



class LatestProducts:
    objects = LatestProductManager()


# Основные таблицы для интернет-магазина
class Category(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', verbose_name='Категория')
    name = models.CharField(max_length=155, verbose_name='Название')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


# Категории
class LaptopsCategory(Product):
    lap_ram = models.CharField(max_length=255, verbose_name='Оперативаня память')
    video_adapter = models.CharField(max_length=255, verbose_name='Видеокарта')
    display = models.CharField(max_length=255, verbose_name='Дисплей')
    disk_memory = models.CharField(max_length=255, verbose_name='Память')
    core = models.CharField(max_length=255, verbose_name='Процессор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'


class SmartPhonesCategory(Product):
    display = models.CharField(max_length=255, verbose_name='Дисплей')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    sd = models.BooleanField()
    memory = models.CharField(max_length=255, verbose_name='Память')
    display_type = models.CharField(max_length=255, verbose_name='Тип экрана')
    phone_core = models.CharField(max_length=255, verbose_name='Процессор', default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'
