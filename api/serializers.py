from rest_framework import serializers
from electronic.models import Category, Manufacturer, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор категорий товара
    """

    class Meta:
        model = Category
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    """
    Сериализатор производителя товара
    """

    class Meta:
        model = Manufacturer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор товара
    """
    gross_cost = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_gross_cost(self, obj):
        return obj.get_cost()
