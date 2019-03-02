from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    mail = serializers.EmailField()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],
            is_staff = validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class StatusSerializer(serializers.ModelSerializer):
    user_mail = serializers.ReadOnlyField(source='user_profile.email')
    user_name = serializers.ReadOnlyField(source='user_profile.name')
    extra_kwargs = {'user_name': {'read_only': True}}
    class Meta:
        model = models.ProfileStatus
        fields = ('id', 'user_profile', 'status_tag', 'status_text', 'created_on', 'user_name', 'user_mail')
        extra_kwargs = {'user_profile': {'read_only': True}}
