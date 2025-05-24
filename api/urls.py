from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('products/', ProductViewSet.as_view(), name='products'),
    path('products/<int:product_id>/', ProductViewSet.as_view(), name='get_product_by_id'),
    path('products/<int:product_id>/', ProductViewSet.as_view(), name='update_product_by_id'),
]