from django.contrib import admin
from .models import FAQSection, Question, BlogSection, Blog, TestimonialSection, Testimonial

# class QuestionInline(admin.TabularInline):
#     model = Question
#     extra = 1  # Number of extra forms to display

admin.site.register(Question)
admin.site.register(FAQSection)
# class FAQSectionAdmin(admin.ModelAdmin):
#     # inlines = [QuestionInline]
#     list_display = ('header', 'include')

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(users=request.user)

#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         if not obj.users.filter(id=request.user.id).exists():
#             obj.users.add(request.user)

# class PostInline(admin.TabularInline):
#     model = Blog
#     extra = 1  # Number of extra forms to display
admin.site.register(Blog)
admin.site.register(BlogSection)
# class BlogSectionAdmin(admin.ModelAdmin):
#     # inlines = [PostInline]

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(users=request.user)

#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         if not obj.users.filter(id=request.user.id).exists():
#             obj.users.add(request.user)
admin.site.register(Testimonial)
admin.site.register(TestimonialSection)
# class TestimonialInline(admin.StackedInline):
#     model = Testimonial
#     extra = 1  # Number of extra forms to display

# class TestimonialSectionAdmin(admin.ModelAdmin):
#     inlines = [TestimonialInline]

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(users=request.user)

#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         if not obj.users.filter(id=request.user.id).exists():
#             obj.users.add(request.user)

# admin.site.register(FAQSection, FAQSectionAdmin)
# admin.site.register(BlogSection, BlogSectionAdmin)
# admin.site.register(TestimonialSection, TestimonialSectionAdmin)
