from django import forms
from django.contrib.auth.models import User
from polls.models import Type, Item


class CartAddItemForm(forms.Form):
    name_person = models.CharField(max_length=20)
    surname_person = models.CharField(max_length=20)
    date_start = models.DateField()
