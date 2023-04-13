from rest_framework import serializers
from herbal.models import Herbal

class HerbalSerializer(serializers.Serializer):
    class Meta:
        model= Herbal
        field ='__all__'