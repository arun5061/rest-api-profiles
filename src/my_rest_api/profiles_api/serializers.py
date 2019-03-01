from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)
    mail = serializers.EmailField()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        print('model:',model)
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):

            user = models.UserProfile(
                name = validated_data.get('name'),
                email = validated_data.get('email'),
            )
            user.set_password(validated_data.get('password'))
            user.save()
            print('ser:',user)
            return user