from .views import (ProductsView, ProductDetailView,
                    LaptopsProductView, SmartphonesProductView,
                    ProductSmartphonesDetailView,
                    )
from django.urls import path


urlpatterns = [
    path('', ProductsView.as_view(), name='list_page'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail_page'),
    path('detail/smart/<int:pk>/', ProductSmartphonesDetailView.as_view(), name='detail_smart_page'),

    path('laptops/', LaptopsProductView.as_view(), name='laptops'),
    path('smartphones/', SmartphonesProductView.as_view(), name='smartphones'),

]

#TODO Доделать в срочно порядке регистрацию и логин в темплате и апдейт юзере через ajax