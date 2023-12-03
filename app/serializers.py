from rest_framework import serializers

from app.models import *
class EMPMS(serializers.ModelSerializer):
    class Meta:
        model=employee_data
        fields="__all__"

