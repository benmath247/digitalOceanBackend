from rest_framework.generics import RetrieveAPIView
from .models import FAQSection, BlogSection
from .serializers import FAQSectionSerializer
from .serializers import BlogSectionSerializer

class FAQSectionViewSet(RetrieveAPIView):
    """
    A viewset that provides the standard actions for FAQSection.
    """
    queryset = FAQSection.objects.all()
    serializer_class = FAQSectionSerializer

class BlogSectionViewSet(RetrieveAPIView):
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionSerializer
