import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import UserProfile

# Create your models here.
class Problem(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(_("name"), max_length=128, blank=True)
    description = models.TextField(blank=True)
    is_solved = models.BooleanField(_("is_solved"), default=False, blank=True)
    problem_solver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='problems', blank=True)


    def __str__(self):
        return self.name

class Question(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    inquiry = models.CharField(_("query"), max_length=100, blank=True)
    response = models.TextField(null=True, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="questions", blank=True)

    def __str__(self):
        return self.inquiry

class Cause(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(_("name"), max_length=128, blank=True)
    description = models.TextField(blank=True)
    is_correct = models.BooleanField(_("is_correct"), default=False)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="causes", blank=True)

    def __str__(self):
        return self.name

class Solution(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(_("name"), max_length=128, blank=True)
    description = models.TextField(blank=True)
    outcome = models.TextField(null=True, blank=True)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, related_name="solutions", blank=True)
    was_tested = models.BooleanField(_("was_tested"), default=False, blank=True)
    is_correct = models.BooleanField(_("is_correct"), default=False, blank=True)

    def __str__(self):
        return self.name
