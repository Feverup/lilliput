from rest_framework import serializers
from .models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):

    short_url = serializers.SerializerMethodField('get_short_url')

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_absolute_url())

    class Meta:
        model = ShortLink
        fields = ('original_url', 'short_url', 'hash', 'created_at', 'updated_at')
