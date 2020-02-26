from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """ serializes name string"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ serializes user profile object"""

    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'password')
        extra_kwargs= {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password',
                }
            }
        }

    def create(self, validated_data):
        """ overwritting original create func to make sure password is hased when stored"""
        user = models.CustomUser.objects.create_user(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
        )
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    """ serializes model feed item """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status', 'created_on')
        extra_kwargs= {
            'user_profile': {
                'read_only': True

            }
        }
