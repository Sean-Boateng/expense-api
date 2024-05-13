from django.db import models

from django.contrib.auth.models import User
from envelope.models import Envelope

class Expense(models.Model):
    envelope = models.ForeignKey(Envelope, on_delete=models.CASCADE, default= '')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    expense_amount = models.DecimalField(max_digits=9, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.envelope.balance -= self.expense_amount
        self.envelope.save()
        super(Expense, self).save(*args, **kwargs)