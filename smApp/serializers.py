from rest_framework import serializers
from .models import schoolInfo


class schoolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolInfo
        fields = [
            "id",
            "schoolName",
            "schoolAddress",
            "schoolEstablished",
            "schoolEstablisher",
        ]
