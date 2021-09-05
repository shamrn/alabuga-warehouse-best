from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView
from electronic.models import Category, Manufacturer, Product
from .serializers import CategorySerializer, ManufacturerSerializer, ProductSerializer
from .filters import TypeManufacturerFilter


class CategoryViewSet(viewsets.ModelViewSet):
    """
    CRUD категории товара
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    CRUD производителя товара
    """

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    filterset_fields = ['name']


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD товара
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = TypeManufacturerFilter


class SummaryProductViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Сумма товара
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = TypeManufacturerFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        get_cost = sum([item.get_cost() for item in queryset])
        data = {'gross_cost': get_cost}
        return Response(data)


class CodeProductView(RetrieveAPIView):

    """
    Вывод товара по уникальному коду
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'code'
