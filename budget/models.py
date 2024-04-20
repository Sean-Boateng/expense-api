from django.db import models
# from authentication.models import User
from django.contrib.auth.models import User

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    balance = models.DecimalField(max_digits=9, decimal_places=2,default=0)
    

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new instance
            self.balance = self.amount  # Set balance to amount if it's a new instance
        super().save(*args, **kwargs)    
    
   