from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,
    ManufacturerViewSet,
    ProductViewSet,
    SummaryProductViewSet,
    CodeProductView )


api_router = routers.DefaultRouter()
api_router.register(r'categories', CategoryViewSet)
api_router.register(r'manufacturers', ManufacturerViewSet)
api_router.register(r'electronics/summary', SummaryProductViewSet)
api_router.register(r'electronics', ProductViewSet)



urlpatterns = [
    path('', include(api_router.urls)),
    path('electronics/code/<code>/', CodeProductView.as_view()),
]