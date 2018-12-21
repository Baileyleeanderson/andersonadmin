from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255)
    birthday = models.DateTimeField(default= datetime.now, blank=True)
    signup_date = models.DateTimeField(default= datetime.now, blank=True)
    date_paid = models.DateTimeField(default= datetime.now, blank=True)
    contract_expiration_date = models.DateTimeField(default= datetime.now, blank=True)
    card_number = models.IntegerField(max_length=50, default=0)
    membership_type = models.CharField(max_length=255, default="Regular")
    kids_club_member = models.CharField(max_length=255, default="No")
    
class Visit(models.Model):
    visit_date = models.DateTimeField(default= timezone.now)
    user_visit = models.ForeignKey(User, related_name='visits', null=True)

class Payments(models.Model):
    payment_date = models.DateTimeField(default= "")
    amount = models.IntegerField(max_length=6, default=0)
    desc = models.CharField(max_length=125, default="")
    user_payment = models.ForeignKey(User, related_name='payments', null=True)

class Walkin(models.Model):
    last_name = models.CharField(max_length=50, default="")
    membership_purchased = models.CharField(max_length=125, default="")
    amount = models.IntegerField(max_length=6, default=0)
    date = models.DateTimeField(default= timezone.now)

class Cafe(models.Model):
    last_name = models.CharField(max_length=50, default="")
    item_purchased = models.CharField(max_length=125, default="")
    amount = models.IntegerField(max_length=6, default=0)
    date = models.DateTimeField(default= timezone.now)

class Expense(models.Model):
    expense_paid_for = models.CharField(max_length=125, default="")
    note = models.CharField(max_length=255, default="")
    amount = models.IntegerField(max_length=6, default=0)
    date = models.DateTimeField(default= timezone.now) 