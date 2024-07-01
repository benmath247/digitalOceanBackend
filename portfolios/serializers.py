from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'section']

class FAQSectionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = FAQSection
        fields = ['id', 'header', 'include', 'questions']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'image', 'title', 'date', 'text', 'section']

class BlogSectionSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = BlogSection
        fields = ['id', 'button', 'include', 'blogs']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'profile_image', "company_image", "testimonial_giver_name", 'testimonial_giver_position']

class TestimonialSectionSerializer(serializers.ModelSerializer):
    testimonials = TestimonialSerializer(many=True, read_only=True)

    class Meta:
        model = TestimonialSection
        fields = ['users', 'testimonials', 'include', 'header', 'subheader']