from django.contrib import admin
from .models import Recipe, Feedback

admin.site.register(Recipe)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text', 'recipe', 'user', 'checked']
    list_editable = ['checked']
    list_filter = ['checked']
    search_fields = ['text']

    fields = ['user', 'recipe', 'text']
    readonly_fields = ['recipe', 'text']



admin.site.register(Feedback, FeedbackAdmin)