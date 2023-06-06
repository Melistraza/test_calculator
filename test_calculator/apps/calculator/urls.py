from django.urls import path
from test_calculator.apps.calculator.views import CalculatorView

urlpatterns = [
    path('calc', CalculatorView.as_view()),
]
