from rest_framework import serializers
from .models import Patient, Procedure, Payment, ReminderLog

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'phone', 'user_id', 'created_at']
