from rest_framework import serializers
from .models import FAQSection, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'section']

class FAQSectionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = FAQSection
        fields = ['id', 'header', 'include', 'questions']
