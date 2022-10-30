from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:id>/<slug:slug>/', views.product_details, name='products'),
]
