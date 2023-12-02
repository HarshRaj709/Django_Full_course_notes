from .models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete,sender = Page)
def delete_related_user(sender,instance,**kwargs):
    print('Page post delted')
    dele = instance
    print(dele)
    instance.user.delete()
    