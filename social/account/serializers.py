from rest_framework import serializers
from .models import acc

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = acc
        fields = "__all__"