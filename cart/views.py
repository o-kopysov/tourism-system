from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from polls.models import Type, Item
from .cart import Cart
from .forms import CartAddItemForm
