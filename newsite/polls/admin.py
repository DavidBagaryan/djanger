from django.contrib import admin

from .models import Question, Choice

admin.AdminSite.site_header = 'POLLS ADMIN MFKRS |-{{ AWESOME'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    # question page
    fieldsets = [
        # (field_set_title, {input_name: model_property}, how_to_display)
        (None, {'fields': ['question_text']}),
        ('Date info', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # add relation models to Question
    inlines = [ChoiceInline]

    # columns to display in list
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # side filter field
    list_filter = ('pub_date',)

    # search field
    search_fields = ('question_text',)

    # items per page
    list_per_page = 3


admin.site.register(Question, QuestionAdmin)
