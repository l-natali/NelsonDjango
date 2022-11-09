from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/<int:product_id>/', views.wishlist_add, name='cart_add'),
    path('remove/<int:product_id>/', views.wishlist_remove, name='cart_remove'),
]
