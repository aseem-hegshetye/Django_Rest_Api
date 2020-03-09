from rest_framework import serializers
from profiles.models import Profile, ProfileStatus


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)  # create seperate serializer for avatar update

    class Meta:
        fields = '__all__'
        model = Profile


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('avatar',)
        model = Profile


class ProfileStatusSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = ProfileStatus
