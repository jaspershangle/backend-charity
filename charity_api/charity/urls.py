from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.ListUser.as_view()),
    path('users/<int:pk>/', views.DetailUser.as_view()),
    path('charities/', views.ListCharity.as_view()),
    path('charities/<int:pk>/', views.DetailCharity.as_view()),
    path('campaigns/', views.ListCampaign.as_view()),
    path('campaigns/<int:pk>/', views.DetailCampaign.as_view()),
    path('sponsers/', views.ListSponser.as_view()),
    path('sponsers/<int:pk>/', views.DetailSponser.as_view()),
    path('donations/', views.ListDonation.as_view()),
    path('donations/<int:pk>/', views.DetailDonation.as_view()),
]