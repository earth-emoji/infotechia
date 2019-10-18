from django.contrib import admin
from django.db import models
from mdeditor.widgets import MDEditorWidget

from .models import Tutorial, Category

# Register your models here.
class TutorialModelAdmin (admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register (Tutorial, TutorialModelAdmin)
admin.site.register(Category)
