from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с товарами.

    Стандартные операции:
    - GET    /api/products/         — список
    - POST   /api/products/         — создание
    - GET    /api/products/{id}/    — детали
    - PUT    /api/products/{id}/    — полное обновление
    - PATCH  /api/products/{id}/    — частичное обновление
    - DELETE /api/products/{id}/    — удаление

    Кастомные операции:
    - POST   /api/products/import_feed/  — импорт списка товаров из JSON-фида
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['post'], url_path='import_feed')
    def import_feed(self, request):
        """Импорт списка товаров из JSON-фида."""

        data = request.data

        # Проверка: должен быть список
        if not isinstance(data, list):
            return Response(
                {'error': 'Ожидается JSON-массив товаров.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not data:
            return Response(
                {'error': 'Список товаров пуст.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        created = []
        errors = []

        for index, item in enumerate(data):
            serializer = self.get_serializer(data=item)
            if serializer.is_valid():
                serializer.save()
                created.append(serializer.data)
            else:
                errors.append({
                    'index': index,
                    'sku': item.get('sku', '—'),
                    'errors': serializer.errors,
                })

        return Response(
            {
                'total': len(data),
                'created': len(created),
                'failed': len(errors),
                'created_items': created,
                'errors': errors,
            },
            status=status.HTTP_201_CREATED if created else status.HTTP_400_BAD_REQUEST,
        )
