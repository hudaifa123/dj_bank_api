from core.models import Currency

Currency.objects.bulk_create(
    [
        Currency(code="USD", name="United States Dollar"),
        Currency(code="EUR", name="Euro"),
        Currency(code="TRL", name="Turkish"),
    ],
)

Currency.objects.all()
