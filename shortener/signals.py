from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from numconv import NumConv
from .models import ShortLink


@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=ShortLink)
def update_hash(sender, instance, **kwargs):
    if not instance.hash:
        instance.hash = NumConv(64).int2str(instance.id)
        instance.save()
