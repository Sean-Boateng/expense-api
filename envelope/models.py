from django.db import models
# from authentication.models import User
from django.contrib.auth.models import User

class Envelope(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    

    
    
   