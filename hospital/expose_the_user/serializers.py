from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    last_login = serializers.Field()
    date_joined = serializers.Field()

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_superuser',
            'is_active',
            'last_login',
            'date_joined',
        )

        write_only_fields = ('password',)
