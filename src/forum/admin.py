from django.contrib import admin
from django.db import models
from mdeditor.widgets import MDEditorWidget

from .models import Thread, Topic

# Register your models here.
class ThreadModelAdmin (admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register (Thread, ThreadModelAdmin)
admin.site.register(Topic)
