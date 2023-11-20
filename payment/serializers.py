from rest_framework import serializers

from .models import Payments


class PaymentsSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	
	class Meta:
		model = Payments
		fields = ['user','price','created_at']