from rest_framework.generics import RetrieveAPIView
from .models import FAQSection
from .serializers import FAQSectionSerializer

class FAQSectionViewSet(RetrieveAPIView):
    """
    A viewset that provides the standard actions for FAQSection.
    """
    queryset = FAQSection.objects.all()
    serializer_class = FAQSectionSerializer
