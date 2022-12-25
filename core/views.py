from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Category, Currency, Transaction
from core.serializers import CategorySerializer, CurrencySerializer, WriteTransactionSerializer, ReadTransactionSerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class TransactionModelViewSet(ModelViewSet):
    # queryset = Transaction.objects.select_related("category", "currency", "user")
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["currency__code"]
    ordering_fields = ["amount"]

    def get_queryset(self):
        return Transaction.objects.select_related(
            "category",
            "currency",
            "user",
        ).filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
