from rest_framework import serializers
from .models import MedicalConsultation


class MedicalConsultationSerializer(serializers.ModelSerializer):
    doctor = serializers.Field()
    date_performed = serializers.Field()

    class Meta:
        model = MedicalConsultation
        fields = (
            'doctor',
            'patient',
            'prescription',
            'diagnosis',
            'is_inpatient',
            'date_performed',
        )
