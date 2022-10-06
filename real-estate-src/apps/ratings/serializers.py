from rest_framework import serializers

from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rated_by = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_rated_by(self, obj):
        return obj.rated_by.username

    def get_agent(self, obj):
        return obj.agent.user.username
