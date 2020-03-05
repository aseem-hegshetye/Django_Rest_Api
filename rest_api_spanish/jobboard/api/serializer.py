from rest_framework import serializers
from ..models import *


class JobBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobBoard
        fields = '__all__'

