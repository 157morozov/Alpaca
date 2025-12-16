from rest_framework import serializers
from main.models import Test


class TestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000,
                                        allow_null=True,
                                        required=False)

    def create(self, validated_data):
        return Test.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
