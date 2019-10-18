import uuid
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfileManager(models.Manager):
    use_for_related_fields = True


class UserProfile(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE, blank=True)
    objects = UserProfileManager()

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __str__(self):
        return self.user.username

