from django.urls import path
from .views import *

urlpatterns = [
    path('faq/<int:pk>/', FAQSectionViewSet.as_view(), name='faq-section-detail'),
    path('blog/<int:pk>/', BlogSectionViewSet.as_view(), name='blog-section-detail'),
    path('testimonials/<int:pk>/', TestimonialSectionViewSet.as_view(), name='blog-section-detail')
]
