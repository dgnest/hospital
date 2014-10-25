from rest_framework import serializers
from .models import Medicine, MedicinePerConsultation


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = (
            'code',
            'name',
            'description',
            'medicine_type',
            'amount',
        )


class MedicinePerConsultationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicinePerConsultation
        fields = (
            'medical_consultation',
            'medicine',
            'amount',
        )
