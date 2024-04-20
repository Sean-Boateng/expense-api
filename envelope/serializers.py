from rest_framework import serializers
from .models import Envelope

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class EnvelopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envelope
        fields = ['id', 'budget', 'name', 'amount']
        depth = 1
