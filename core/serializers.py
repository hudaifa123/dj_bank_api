from rest_framework import serializers
from core.models import Category, Currency, Transaction
from django.contrib.auth.models import User


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]
        read_only_fields = fields


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            "id",
            "code",
            "name",
        )


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = (
            "id",
            "user",
            "name",
        )


class WriteTransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "user",
            "category",
            "currency",
            "descriptions",
            "date",
        )

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        user = self.context["request"].user
        self.fields["category"].queryset = user.categories.all()


class ReadTransactionSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "user",
            "category",
            "currency",
            "descriptions",
            "date",
        )
        read_only_fields = fields
