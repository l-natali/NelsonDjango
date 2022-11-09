from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:id>/<slug:slug>/', views.blog_details, name='posts'),
]
