from rest_framework import serializers
from rest_framework.serializers import ModelSerializer 
from ..models import Image
import base64

class ImageSerializer(ModelSerializer):

    # Overrides default encoding ansd decoding for this field
    image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = "__all__"

    def get_image(self, obj):
        if obj.image:
            return base64.b64encode(obj.image).decode('utf-8')
        return None
    
    def to_internal_value(self, data):
        image_data_base64 = data.get('image', '')
        if image_data_base64:
            format, imgstr = image_data_base64.split(';base64,')
            data['image'] = base64.b64decode(imgstr)
        return super().to_internal_value(data)