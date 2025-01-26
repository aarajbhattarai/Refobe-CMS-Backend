
from rest_framework import serializers
from travelpackage.models import TravelPackage, PricingRule


class PricingRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRule
        fields = ['min_people', 'max_people', 'days', 'price']


class TravelPackageSerializer(serializers.ModelSerializer):
    pricing_rules = PricingRuleSerializer(many=True, read_only=True)

    class Meta:
        model = TravelPackage
        fields = ['id', 'title', 'description', 'base_price', 'duration_days', 'image', 'pricing_rules']
