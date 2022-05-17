from rest_framework import serializers
from core.models import Liquid


class LiquidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Liquid
        fields = (
            'id', 'available', 'title', 'picture', 'url'
        )
