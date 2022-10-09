from rest_framework import serializers
from apps.ratings.serializers import RatingSerializer
from .models import Profile
from django_countries.serializer_fields import CountryField


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    full_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(source="user.email")
    country = CountryField(name_only=True)
    ratings = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "about_me",
            "license_number",
            "profile_photo",
            "gender",
            "country",
            "city",
            "is_buyer",
            "is_seller",
            "is_agent",
            "num_reviews",
            "ratings",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_ratings(self, obj):
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation["top_agent"] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "about_me",
            "license_number",
            "profile_photo",
            "gender",
            "country",
            "city",
            "is_buyer",
            "is_seller",
            "is_agent",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation["top_agent"] = True
        return representation
