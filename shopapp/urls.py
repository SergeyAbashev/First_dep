from django.urls import path, include
from .views import (
    ShopIndexView,
)

app_name = 'shopapp'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index')
]
