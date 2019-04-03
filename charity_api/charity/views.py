from rest_framework import generics

from .models import User, Charity, Campaign, Sponser, Donation
from .serializers import UserSerializer, CharitySerializer, CampaignSerializer, SponserSerializer, DonationSerializer

class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCharity(generics.ListCreateAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer

class DetailCharity(generics.RetrieveUpdateDestroyAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer

class ListCampaign(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class DetailCampaign(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class ListSponser(generics.ListCreateAPIView):
    queryset = Sponser.objects.all()
    serializer_class = SponserSerializer

class DetailSponser(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponser.objects.all()
    serializer_class = SponserSerializer

class ListDonation(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class DetailDonation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer