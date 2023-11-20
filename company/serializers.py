from rest_framework import serializers
from collections import OrderedDict

from .models import Locations, Keywords, Ad, Company


class LocationsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Locations
		fields = ['id', 'name']

class KeywordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Keywords
		fields = ['id', 'keyword']

class AdSerializer(serializers.ModelSerializer):
	keywords = KeywordsSerializer(many=True)

	class Meta:
		model = Ad
		fields = [
			'id','headline', 'description', 'ad_type', 'price', 'keywords',
			'impressions','clicks','click_rate','conversions','cost','cpc','cpa']

class CompanySerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	locations = LocationsSerializer(many=True)
	ad = AdSerializer()

	class Meta:
		model = Company
		fields = ['id', 'user', 'locations', 'ad', 'name', 'status','website', 'launge', 'active']

		read_only = ('id','status',)

	def create(self, validated_data):
		locations_data = validated_data.pop('locations', [])
		ad_data = validated_data.pop('ad')

		keywords_data = ad_data.pop('keywords', [])
		ad = Ad.objects.create(**ad_data)

		for keyword_data in keywords_data:
		    keyword = Keywords.objects.create(**keyword_data)
		    ad.keywords.add(keyword)

		company = Company.objects.create(ad=ad, **validated_data)

		for location_data in locations_data:
		    location = Locations.objects.create(**location_data)
		    company.locations.add(location)

		return company

	def update(self, instance, validated_data):
		locations_data = validated_data.pop('locations', [])
		ad_data = validated_data.pop('ad')

		keywords_data = ad_data.pop('keywords', [])

		instance.user = validated_data.get('user', instance.user)
		instance.name = validated_data.get('name', instance.name)
		instance.website = validated_data.get('website', instance.website)
		instance.launge = validated_data.get('launge', instance.launge)
		instance.active = validated_data.get('active', instance.active)

		instance.locations.clear()
		for location_data in locations_data:
			location = Locations.objects.create(**location_data)
			instance.locations.add(location)

		ad = instance.ad
		ad.headline = ad_data.get('headline', ad.headline)
		ad.description = ad_data.get('description', ad.description)
		ad.ad_type = ad_data.get('ad_type', ad.ad_type)
		ad.price = ad_data.get('price', ad.price)

		ad.keywords.clear()
		for keyword_data in keywords_data:
			keyword = Keywords.objects.create(**keyword_data)
			ad.keywords.add(keyword)

		ad.save()
		instance.save()

		return instance
