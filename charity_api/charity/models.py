from django.db import models

class User(models.Model):
  username = models.CharField(max_length=255)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField()
  code = models.CharField(max_length=50, unique=True)
  def __str__(self):
        return self.username

class Charity(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField()
  bio = models.TextField()
  website = models.URLField(null=True)
  owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL, related_name='charities')
  def __str__(self):
        return self.name

class Donation(models.Model):
  donator = models.ForeignKey('User', null=True, on_delete=models.SET_NULL,related_name='donations')
  charity = models.ForeignKey('Charity', null=True, on_delete=models.SET_NULL,related_name='donations')
  influencer = models.ForeignKey('User', null=True, on_delete=models.SET_NULL,related_name='donations_influenced')
  campaign = models.ForeignKey('Campaign', null=True, on_delete=models.SET_NULL,related_name='donations')
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  anonymous = models.BooleanField(default=False)
  def __str__(self):
        return f'{self.donator}, {self.charity}, {self.amount}'

class Campaign(models.Model):
  charity = models.ForeignKey('Charity', null=True, on_delete=models.SET_NULL,related_name='campaigns')
  sponser = models.ForeignKey('Sponser', null=True, on_delete=models.SET_NULL,related_name='campaigns')
  owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL, related_name='campaigns')
  reward = models.TextField(default='None')
  goal = models.DecimalField(max_digits=8, decimal_places=2)
  raised = models.DecimalField(max_digits=8, decimal_places=2)
  start_date = models.DateField()
  end_date = models.DateField()
  def __str__(self):
        return f'{self.charity}, {self.sponser}'

class Sponser(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField()
  website = models.URLField(null=True)
  bio = models.TextField()
  owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL, related_name='sponsers')
  def __str__(self):
        return self.name
