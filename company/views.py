from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import CompanySerializer
from .models import Company


@api_view(['POST'])
def create_company(request):
	""" Create a company for the user """
	serializer = CompanySerializer(data=request.data, context={'request': request})
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response(serializer.data, status=201)

	return Response(serializer.errors, status=400)

@api_view(['GET'])
def user_companies(request):
	""" User display companies """
	company = Company.objects.filter(user=request.user, active=True)
	serializer = CompanySerializer(company, many=True)
	return Response(serializer.data, status=200)


class DetailCompanyView(APIView):
	serializer_class = CompanySerializer

	def get_object(self, request, id):
		try:
			return Company.objects.get(id=id, user=request.user)
		except Company.DoesNotExist:
			raise Http404

	def get(self, request, id):
		company = self.get_object(request, id)
		serializer = self.serializer_class(company)
		return Response(serializer.data, status=200)

	def put(self, request, id):
		company = self.get_object(request, id)
		serializer = self.serializer_class(instance=company, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)

		return Response(serializer.errors, status=400)

	def delete(self, request, id):
		company = self.get_object(request, id)
		company.active = False
		company.save()
		return Response({'ok':True}, status=200)