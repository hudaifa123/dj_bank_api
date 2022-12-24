from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from core.models import Category, Currency
from core.serializers import CategorySerializer, CurrencySerializer


class CurrencyListAPIView(ListAPIView):
     queryset = Currency.objects.all()
     serializer_class = CurrencySerializer
     
     
class CategoryModelViewSet(ModelViewSet):
     queryset = Category.objects.all()
     serializer_class = CategorySerializer
