from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as TokenView
from core import views


router = routers.SimpleRouter()
router.register(r"categories", views.CategoryModelViewSet, basename="category")
router.register(r"transactions", views.TransactionModelViewSet, basename="transaction")
router.register(r"currencies", views.CurrencyModelViewSet, basename="currencies")


urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("login/", TokenView.obtain_auth_token, name="obtain-auth-token"),
    path("reports/", views.TransactionReportAPIView.as_view(), name="reports"),
]

urlpatterns += router.urls
