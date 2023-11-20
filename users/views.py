from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer
from .models import Users


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
	""" user create """
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		user = serializer.save()
		# create token
		token, _ = Token.objects.get_or_create(user=user)
		return Response({'token':token.key}, status=201)

	return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def login(request, email, password):
	""" login """
	try:
		user = Users.objects.get(email=email, password=password)
		token = Token.objects.get(user=user)
		return Response({'token':token.key}, status=200)
	except Users.DoesNotExist:
		return Response({'error':'Email or password is incorrect.'}, status=400)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def activate(request, code):
	""" user activate (email verification) """
	user = request.user
	if user.confirmation_code == code:
		user.active = True
		user.save()
		return Response({'ok':True}, status=200)

	return Response({'error':'The verification code is invalid.'}, status=400)

class UserProfileView(APIView):
	serializer_class = UserSerializer

	def get(self, request):
		serializer = self.serializer_class(request.user)
		return Response(serializer.data, status=200)

	def put(self, request):
		serializer = self.serializer_class(instance=request.user, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)

		return Response(serializer.errors, status=400)