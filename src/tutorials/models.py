import datetime
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from mdeditor.fields import MDTextField

# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    # a2.parent = a1; a1.children.all()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tutorial(models.Model):
    title = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    video = models.URLField(max_length=250, null=True, blank=True)
    content = MDTextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tutorials', blank=True)
    categories = models.ManyToManyField(Category, related_name='tutorials', blank=True)

    class Meta:
        verbose_name = _('tutorial')
        verbose_name_plural = _('tutorials')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        today = datetime.datetime.today()
        title_slugified = slugify(self.title)
        self.slug = f'{today:%Y%m%d%M%S}-{title_slugified}'
        super().save(*args, **kwargs)
