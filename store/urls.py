from .views import (ProductsView, ProductDetailView,
                    LaptopsProductView, SmartphonesProductView,
                    ProductSmartphonesDetailView, RegisterView,
                    UserProfileView, UserProfileUpdateView
                    )
from django.urls import path
from .views import UserLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', ProductsView.as_view(), name='list_page'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail_page'),
    path('detail/smart/<int:pk>/', ProductSmartphonesDetailView.as_view(), name='detail_smart_page'),

    path('laptops/', LaptopsProductView.as_view(), name='laptops'),
    path('smartphones/', SmartphonesProductView.as_view(), name='smartphones'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name ='profile'),
    path('profile/update/<int:pk>/', UserProfileUpdateView.as_view(), name='update_user'),
]

#TODO Доделать в срочно порядке регистрацию и логин в темплате и апдейт юзере через ajax