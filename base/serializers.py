from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    
	password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})

	class Meta:
		model = CustomUser
		fields = ['email', 'username', 'password']
	def create(self, validated_data):
		user_password = validated_data.get('password', None)
		db_instance = self.Meta.model(email=validated_data.get('email'), username=validated_data.get('username'))
		db_instance.set_password(user_password)
		db_instance.save()
		return db_instance
