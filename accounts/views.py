from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, EditAccountForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST
from polls.models import Type, Item
from cart.cart import Cart
from cart.forms import CartAddItemForm

def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('own_account')

@require_POST
def cart_add(request, type_id):
    cart = Cart(request)
    type = get_object_or_404(Type,type_id=id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        name_person = form.cleaned_data.get('name_person')
        surname_person = form.cleaned_data.get('surname_person')
        date_start = form.cleaned_data.get('date_start')
    item = Item(type_tiket = type , name_person=name_person, surname_person = surname_person, date_start= date_start)
    #item.save()
    cart.add(item)
    return redirect('own_account')

def type_detail(request, pk):
    type = get_object_or_404(Type, pk=id)
    cart_item_form = CartAddItemForm()
    return render(request, 'detail.html', {'type_ticket': type, 'cart_item_form': cart_item_form})

def create_item(request, id ):
    type = get_object_or_404(Type, id=id)
    item = create(type_tiket = type , name_person="name_person", surname_person = "surname_person", date_start = date.today)
    return render(request, 'detail.html', {'item': item})

def own_account(request):
    return render(request,'account.html')
# own_account(request):
    #cart = Cart(request)
    #return render(request, 'account.html', {'cart': cart})

def signup(response):
    if response.method == "POST":
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(response, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(response, 'signup.html', {'form': form})




def edit_account(response):
    if response.method == "POST":
        form = EditAccountForm(response.POST, instance=response.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/account')
    else:
        form = EditAccountForm(instance=response.user)
    return render(response, 'edit_account.html',{"form": form})

def change_password(response):
    if response.method == "POST":
        form = PasswordChangeForm(data=response.POST, user=response.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(response, form.user)
            return redirect('/accounts/account')
        else:
            return redirect('/accounts/account/change_password')
    else:
        form = PasswordChangeForm(user=response.user)
    return render(response, 'change_password.html',{"form": form})
