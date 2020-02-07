from django.db import models
from django.utils import timezone
# Create your models here.

class CrackedUsers(models.Model):
	name = models.CharField(max_length=100)
	profile_link = models.URLField()
	solved_on = models.DateTimeField(default=timezone.now)

