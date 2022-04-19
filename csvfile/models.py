from datetime import datetime
import django
from django.db import models
from datetime import date
from datetime import time



class File(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    institution_name = models.CharField(default=False,max_length=100)
    date_now =models.DateField(default=datetime.now())
    timing = models.TimeField(default=datetime.now())
    # created_at = models.DateTimeField(auto_now_add=True)
    # timing = models.TimeField(default=django.utils.timezone.now())
    visited= models.BooleanField(default=False)

    def __str__(self):
        return self.id