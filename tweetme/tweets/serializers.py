from rest_framework import serializers
from .models import TweetModel
from django.conf import settings

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = [
            'content',
            # 'id'
            ]
    def validate_content(self, value):
        if len(value)>settings.MAX_TWEET_LENGTH:
            raise serializers.ValidationError("Content too long")
        return value

class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in settings.TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError(
                f'Invalid action: {value} is not in {settings.TWEET_ACTION_OPTIONS}'
            )
