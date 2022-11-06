"""nelson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.views import base, shop, about, faq, compare, product_details, cart, checkout, wishlist, my_account, login
from base.views import blog, blog_details, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('home/', base, name='home'),
    path('shop/', include('base.urls', namespace='shop')),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('compare/', compare, name='compare'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
    path('my-account/', my_account, name='my-account'),
    path('login-register/', login, name='login-register'),
    path('blog/', blog, name='blog'),
    path('blog-details/', blog_details, name='blog-details'),
    path('contact/', contact, name='contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
