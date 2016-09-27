from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Item, ItemManager
from ..new_login.models import User

# Create your views here.
def index(request):
    all_items = Item.objects.all()
    this_user_items = Item.objects.filter(user_other=request.session['id'])
    this_user = User.objects.get(id=request.session['id'])
    other_items = Item.objects.exclude(user_created=this_user)

    context = {
        'all_items': all_items,
        'this_user': this_user,
        'other_items':other_items,
        'this_user_items':this_user_items
    }
    return render(request, 'djangoDemo/index.html', context)

def new(request):
    this_user = User.objects.get(id=request.session['id'])
    context = {
        'this_user': this_user
    }
    return render(request, 'djangoDemo/addItem.html', context)

def show(request, id):
    this_item = Item.objects.get(id=id)
    result = Item.objects.filter(item_name=this_item.item_name)
    context = {
        'name':this_item,
        'this_item': result
    }
    return render(request, 'djangoDemo/show.html', context)

def addItem(request):
    if request.method == 'POST':
        user_id = request.session['id']
        item = Item.objects.addItem(request.POST, user_id)
        if item['added']:
            new_item = item['new_item']
            messages.success(request, new_item.item_name + " was Successfully added to Wish List")
        else:
            for error in item['errors']:
                messages.error(request, error)
    return redirect(reverse('wishlist:index'))

def add_to_wishlist(request):
    if request.method =='POST':
        user_id = request.session['id']
        item_add = Item.objects.addwishlist(request.POST, user_id)
        if item_add['added']:
            messages.success(request, "Item Successfully added to Wishlist")
    return redirect(reverse('wishlist:index'))


def remove_from_wishlist(request, id):
    if request.method == 'POST':
        remove_item = Item.objects.get(id=id)
        print remove_item
        remove_item.delete()
        messages.success(request, remove_item.item_name + " was removed from WishList")
    return redirect(reverse('wishlist:index'))


def delete(request, id):
    Item.objects.get(id=id).delete()
    return redirect(reverse('wishlist:index'))

def logOut(request):
    request.session.clear()
    return redirect(reverse('users:index'))
