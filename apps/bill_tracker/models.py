from django.db import models
from apps.travel.models import User

# Create your models here.

class Bill(models.Model):
    desc = models.CharField(max_length=128, null=False)
    amount = models.FloatField(null=False)
    user = models.ForeignKey(User, related_name='has_bills', on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

