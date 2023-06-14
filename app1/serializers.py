from app1.models import *
from rest_framework import serializers

class productserializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
