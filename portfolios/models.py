from django.db import models, utils
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
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
    
class BlogSection(models.Model):
    users = models.ManyToManyField(User)
    include = models.BooleanField(default=True)
    button = models.CharField(max_length=300, null=True, blank=True, default="View all blogs")

    def __str__(self):
        return "blog:" + self.button

class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    title = models.CharField(max_length=300, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    text = RichTextField(null=True, blank=False)
    section = models.ForeignKey(BlogSection, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title
    
class TestimonialSection(models.Model):
    users = models.ManyToManyField(User)
    include = models.BooleanField(default=True)
    header = models.CharField(max_length=300, null=True, blank=True, default="View all blogs")
    subheader = models.CharField(max_length=300, null=True, blank=True, default="View all blogs")

    def __str__(self):
        return self.header + " - " + self.subheader


class Testimonial(models.Model):
    section = models.ForeignKey(TestimonialSection, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(null=True, blank=True)
    company_image = models.ImageField(null=True, blank=True)
    testimonial_giver_name = models.CharField(max_length=300, null=False, blank=False)
    testimonial_giver_position = models.CharField(max_length=300, null=False, blank=False)
    testimonial_text = RichTextField(null=True, blank=False)
    slug = models.SlugField(max_length=300, unique=True, blank=True)

    def __str__(self):
        return self.testimonial_giver_name

    def save(self, *args, **kwargs):
        try:
            if not self.slug:
                self.slug = slugify(self.testimonial_giver_name)
        except utils.IntegrityError:
            self.slug += self.id

        super(Testimonial, self).save(*args, **kwargs)
