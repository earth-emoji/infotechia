import datetime
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Topic(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('topic')
        verbose_name_plural = _('topics')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Thread(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    subject = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='threads', blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='threads', blank=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        today = datetime.datetime.today()
        subject_slugified = slugify(self.subject)
        self.slug = f'{today:%Y%m%d%M%S}-{subject_slugified}'
        super().save(*args, **kwargs)