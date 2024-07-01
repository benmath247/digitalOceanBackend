from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class FAQSection(models.Model):
    users = models.ManyToManyField(User)
    include = models.BooleanField(default=True)
    header = models.CharField(max_length=300, null=True, blank=True, default="FAQ")

    def __str__(self):
        return self.header

class Question(models.Model):
    question = models.CharField(max_length=350, null=True, blank=False)
    answer = RichTextField(null=True, blank=False)
    section = models.ForeignKey(FAQSection, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question
