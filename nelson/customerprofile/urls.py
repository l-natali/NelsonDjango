from django.urls import path
from .views import CustomerProfileView, CustomerRegistrationView, CustomerLogoutView, CustomerLoginView

app_name = 'customerprofile'

urlpatterns = [
    path('', CustomerProfileView.as_view(), name='customerprofile'),
    path('register/', CustomerRegistrationView.as_view(), name='register'),
    path('logout/', CustomerLogoutView.as_view(), name='logout'),
    path('login/', CustomerLoginView.as_view(), name='login'),
]
