from rest_framework import serializers
from .models import Dogbook


class DogbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dogbook
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )
