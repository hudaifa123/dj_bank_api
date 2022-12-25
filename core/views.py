from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, permissions, views, response
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Category, Currency, Transaction
from core.permissions import IsAdminOrReadOnly
from core.reports import transaction_report
from core.serializers import (
    ReportEntrySerializer,
    ReportParametersSerializer,
    CategorySerializer,
    CurrencySerializer,
    WriteTransactionSerializer,
    ReadTransactionSerializer,
)


class TransactionReportAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        params_serializer = ReportParametersSerializer(data=request.GET, context={"request": request})
        params_serializer.is_valid(raise_exception=True)
        params = params_serializer.save()
        data = transaction_report(params)
        serializer = ReportEntrySerializer(instance=data, many=True)
        return response.Response(data=serializer.data)


class CurrencyModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None
    renderer_classes = [JSONRenderer]


class CategoryModelViewSet(ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
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
