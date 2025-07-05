from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseIncomeViewSet, RegisterView

router = DefaultRouter()
router.register(r'expenses', ExpenseIncomeViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
]
