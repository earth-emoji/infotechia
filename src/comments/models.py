from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from tutorials.models import Tutorial
from forum.models import Thread

# Create your models here.
class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', blank=True)

    class Meta:
        verbose_name = _('comments')
        verbose_name_plural = _('comments')
        ordering = ('created',)

    def __str__(self):
        return f'{self.pk}-{self.creator.username}'