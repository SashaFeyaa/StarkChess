from rest_framework import serializers
from user_profile.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['wallet_address', 'score', 'profile_pic_num']

class TopUsersSerializer(serializers.Serializer):
    users = UserSerializer(many=True)
    current_user = UserSerializer()