from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blog


@receiver(post_save, sender=Blog)
def post_saved_handler(sender, instance, created, **kwargs):
    if created:
        print(f"New Post has been created: {instance.title}")
        print(sender, instance, created)
    else:
        print(f"Post has been updated: {instance.title}")
