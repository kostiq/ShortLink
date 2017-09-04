from django.db import models
from django.utils import timezone


class Links(models.Model):
	link = models.CharField(max_length=512)
	created = models.DateTimeField(default=timezone.now)
	short_link = models.CharField(max_length=10, blank=True, null=True)