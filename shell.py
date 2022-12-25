from core.models import Currency

Currency.objects.bulk_create(
    [
        Currency(code="USD", name="United States Dollar"),
        Currency(code="EUR", name="Euro"),
        Currency(code="TRL", name="Turkish"),
    ],
)

Currency.objects.all()


from core.models import Transaction, Currency, Category
import random
from decimal import Decimal
from django.utils import timezone

txs = []
currencies = list(Currency.objects.all())
categories = list(Category.objects.all())

# for i in range(1, 1000):
#     c = random.choice(currencies)
#     txs.append(
#         Transaction(
#             date=timezone.now(),
#             amount=Decimal(random.randint(1, 100)),
#             currency=c,
#             category=random.choice(categories),
#             descriptions="Transaction %s" % i,
#         )
#     )
#     c.save()


for i in range(2, 1000):
    tx=Transaction(
        amount=random.randrange(Decimal(1), Decimal(1000)), 
        currency=random.choice(currencies), 
        descriptions="descriptions with django shell", 
        date=timezone.now() - timezone.timedelta(days=random.randint(1, 365)), 
        category=random.choice(categories)
    )
    txs.append(tx)
    len(txs)

Transaction.objects.bulk_create(txs)


# {
#   "username": "Maria",
#   "password": "Your password can’t be entirely numeric."
# }