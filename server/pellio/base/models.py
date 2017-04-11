from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms

class GratitudeJournalEntry(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField('Date')
    journal_entry = models.TextField()


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(
        required = True,
        label = 'first_name',
        max_length = 32
    )
    last_name = forms.CharField(
        required = True,
        label = 'last_name',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
