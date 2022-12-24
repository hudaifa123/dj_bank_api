from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Category, Currency, Transaction
from core.serializers import CategorySerializer, CurrencySerializer, WriteTransactionSerializer, ReadTransactionSerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.select_related("category", "currency")
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["currency__code"]
    ordering_fields = ["amount"]
    # serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
