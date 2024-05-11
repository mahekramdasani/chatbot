from rest_framework import serializers
from .models import CustomUser, Chat
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password', 'tokens')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        return super(UserSerializer, self).create(validated_data)

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'user', 'message', 'response', 'timestamp')
