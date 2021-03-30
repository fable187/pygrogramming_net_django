from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    # the following adjusts the order of the columns
    # fields = ["tutorial_published",
    #           "tutorial_title",
    #           "tutorial_content"]

    # here we instead of just re-ordering the columns, we seperate the columns into sections:
    # Title/date
    # Content
    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Tutorial, TutorialAdmin)
