from django.db import models
from datetime import datetime

# Create your models here.

class Email(models.Model):
    signup_email    =   models.EmailField(max_length=100)
    created_at      =   models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.signup_email