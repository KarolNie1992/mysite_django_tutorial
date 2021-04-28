from django.contrib import admin

from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)


class ChoiceInline (admin.TabularInline):
    """
    StackedInline, TabularInline
    """
    model = Choice
    extra = 3


class QuestionAdmin (admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {
                                    'fields': ['pub_date'],
                                    'classes': ['collapse']
                                }
        ),
    ]
    search_fields = ['question_text']
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
