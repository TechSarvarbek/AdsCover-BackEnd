from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Payments
from .serializers import PaymentsSerializer


@api_view(['POST'])
def pay_create(request):
	serializer = PaymentsSerializer(data=request.data, context={'request':request})
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=200)

	return Response(serializer.errors, status=400)


@api_view(['GET'])
def payments(request):
	user_payments = Payments.objects.filter(user=request.user)
	serializer = PaymentsSerializer(user_payments, many=True)
	return Response(serializer.data, status=200)