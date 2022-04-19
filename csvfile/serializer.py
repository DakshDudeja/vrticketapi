from rest_framework import serializers
from . import models

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = models.File
        fields = "__all__"
