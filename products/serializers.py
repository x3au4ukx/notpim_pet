from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.
    """

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_price(self, value):
        """Проверяем, что цена положительная."""
        if value <= 0:
            raise serializers.ValidationError(
                'Цена должна быть больше 0.'
            )
        return value

    def validate_sku(self, value):
        """Проверяем, что SKU не пустой."""
        if not value.strip():
            raise serializers.ValidationError(
                'SKU не может быть пустым.'
            )
        return value.strip().upper()
