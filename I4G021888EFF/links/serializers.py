from rest_framework import serializers

from I4G021888EFF.links.models import Link
from .models import Link
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'