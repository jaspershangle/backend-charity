from django.contrib import admin

from .models import User, Charity, Campaign, Sponser, Donation

Models = (User, Charity, Campaign, Sponser, Donation)
admin.site.register(Models)