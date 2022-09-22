from django.contrib import admin
from django.contrib.auth.models import User , Group

from .models import Card

admin.site.register(Card)
admin.site.unregister(User)
admin.site.unregister(Group)
