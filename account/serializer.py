from rest_framework import serializers
from django.contrib.auth.models import User


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': ('User already exits')})
        return super().validate(args)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# User serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
