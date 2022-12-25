from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as TokenView
from core import views


router = routers.SimpleRouter()
router.register(r"categories", views.CategoryModelViewSet, basename="category")
router.register(r"transactions", views.TransactionModelViewSet, basename="transaction")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", TokenView.obtain_auth_token, name="obtain-auth-token"),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
]

urlpatterns += router.urls
