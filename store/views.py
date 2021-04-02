from django.views import generic
from .models import (Product, LatestProducts,
                     LaptopsCategory, SmartPhonesCategory)



class ProductsView(generic.ListView):
    template_name = 'products/main_page.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = LatestProducts.objects.get_last_products('laptopscategory', 'smartphonescategory')[:6]
        return context


class ProductDetailView(generic.DetailView):
    template_name = 'products/detail_laptop.html'
    model = LaptopsCategory


class ProductSmartphonesDetailView(generic.DetailView):
    template_name = 'products/detail_smart.html'
    model = SmartPhonesCategory



# Фильтер
class LaptopsProductView(generic.ListView):
    template_name = 'products/laptops.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(LaptopsProductView, self).get_context_data(**kwargs)
        context['laptops'] = LaptopsCategory.objects.all().order_by('-id')
        return context


class SmartphonesProductView(generic.ListView):
    template_name = 'products/smartphones.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(SmartphonesProductView, self).get_context_data(**kwargs)
        context['smartphones'] = SmartPhonesCategory.objects.all().order_by('-id')
        return context