from rest_framework import serializers
from .models import RiskType, RiskFormField, RiskFormFieldOption



class RiskTypeSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = RiskType
        fields = "__all__"


    def save(self):
        user =  self.context['request'].user
        self.validated_data['owner'] = user
        return super().save()


class RiskFormFieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFormFieldOption
        fields = "__all__"


class RiskFormFieldSerializer(serializers.ModelSerializer):
    options = RiskFormFieldOptionSerializer(many=True, read_only=True)
    class Meta:
        model = RiskFormField
        fields = "__all__"
