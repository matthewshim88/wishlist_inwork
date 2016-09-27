from __future__ import unicode_literals
from django.db import models
from ..new_login.models import User

from django.db import models

class ItemManager(models.Manager):
    def addItem(self, data, user_id):
        response = {}
        errors = self.validateItem(data)
        if len(errors) > 0:
            response['added'] = False
            response['errors'] = errors
        else:
            user = User.objects.get(id=user_id)
            new_item = Item.objects.create(item_name = data['name'], user_created=user)
            response['added'] = True
            response['new_item'] = new_item
        return response

    def addwishlist(self, data, user_id):
        response = {}
        other_user = User.objects.get(id=user_id)
        new_item = Item.objects.create(item_name=data['item_name'], user_other=other_user)
        response['added'] = True
        response['new_item'] = new_item
        return response


    def validateItem(self, data):
        errors=[]
        #check if wishlist already exists in DB
        existing_item = self.filter(item_name=data['name'])
        if existing_item:
            errors.append('That item is already on the Wishlist')
        if len(data['name']) < 3:
            errors.append('Wishlist item must at least 3 characters')
        return errors


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    user_created = models.ForeignKey(User, related_name='user_created', default=False)
    user_other = models.ForeignKey(User, related_name ='user_other', default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
