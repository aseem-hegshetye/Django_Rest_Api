from rest_framework import serializers
from . import models


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id','username', 'first_name','last_name','email','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
