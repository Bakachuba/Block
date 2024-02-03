from rest_framework import serializers

from blocks.models import Idea, List, Notes, Periodic, Summary


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'



class PeriodicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodic
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'
