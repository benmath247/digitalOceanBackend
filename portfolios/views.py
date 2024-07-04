from rest_framework.generics import RetrieveAPIView
from .models import FAQSection, BlogSection, TestimonialSection
from .serializers import *

class FAQSectionViewSet(RetrieveAPIView):
    """
    A viewset that provides the standard actions for FAQSection.
    """
    queryset = FAQSection.objects.all()
    serializer_class = FAQSectionSerializer

class BlogSectionViewSet(RetrieveAPIView):
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionSerializer

class TestimonialSectionViewSet(RetrieveAPIView):
    queryset = TestimonialSection.objects.all()
    serializer_class = TestimonialSectionSerializer

class TestimonialRetrieveAPIView(RetrieveAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    lookup_field = 'slug'
