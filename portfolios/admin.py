from django.contrib import admin
from .models import FAQSection, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of extra forms to display

class FAQSectionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('header', 'include')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(users=request.user)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not obj.users.filter(id=request.user.id).exists():
            obj.users.add(request.user)

admin.site.register(FAQSection, FAQSectionAdmin)
