from django.db import models
# from authentication.models import User
from django.contrib.auth.models import User
from budget.models import Budget

class Envelope(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if this is a new instance
            self.budget.balance -= self.amount  # Subtract amount from budget.balance
            self.budget.save()  # Save the updated budget balance
        super().save(*args, **kwargs)