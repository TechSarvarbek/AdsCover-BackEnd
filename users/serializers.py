from rest_framework import serializers

from .models import Users



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('email', 'first_name', 'last_name','telegram_name','referral','password',
						'created_at',)

		read_only = ('active',)
