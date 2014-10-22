from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    dni = serializers.CharField(
        source='dni',
        max_length=8,
        min_length=8,
    )
    superuser = serializers.Field()
    date_joined = serializers.Field()

    class Meta:
        model = Patient
        fields = (
            'dni',
            'superuser',
            'first_name',
            'last_name',
            'age',
            'sex',
            'address',
            'email',
            'telephone',
            'cellphone',
            'date_joined',
        )
