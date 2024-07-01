from django.urls import path
from .views import FAQSectionViewSet

urlpatterns = [
    path('faq/<int:pk>/', FAQSectionViewSet.as_view(), name='faq-section-detail'),
]
