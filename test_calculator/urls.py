from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from test_calculator.apps.calculator.urls import urlpatterns as calculator_urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('', include(calculator_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
