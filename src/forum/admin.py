from django.contrib import admin
from django.db import models

from .models import Thread, Topic

admin.site.register (Thread)
admin.site.register(Topic)
