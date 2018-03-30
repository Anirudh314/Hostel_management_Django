from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class room_form(models.Model):
    room_no = models.CharField(max_length=4)
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

def create_form(sender, **kwargs):
    if kwargs['created']:
        user_profile = room_form.objects.create(user=kwargs['instance'])     

post_save.connect(create_form, sender=User)
