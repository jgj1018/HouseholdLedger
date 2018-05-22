from rest_framework import serializers


class CodeSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
      pass

    def create(self, validated_data):
      pass

    code = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
