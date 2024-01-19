from rest_framework import serializers
from blocks.models import Idea, Notes, Periodic


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class PeriodicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodic
        fields = '__all__'
