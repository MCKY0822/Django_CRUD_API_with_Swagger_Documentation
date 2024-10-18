from rest_framework import serializers
from .models import TimeSlot

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'

    def validate_ids(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("The 'ids' field must be a dictionary.")
        return value
