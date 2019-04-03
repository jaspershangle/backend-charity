from rest_framework import serializers
from .models import User, Charity, Campaign, Sponser, Donation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'code'
        )
        model = User

class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'bio',
            'website',
            'owner'
        )
        model = Charity

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'charity',
            'sponser',
            'owner',
            'reward',
            'goal',
            'raised',
            'start_date',
            'end_date'
        )
        model = Campaign

class SponserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'website',
            'bio',
            'owner',
        )
        model = Sponser

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'donator',
            'charity',
            'influencer',
            'amount',
            'anonymous',
            'campaign'
        )
        model = Donation
  