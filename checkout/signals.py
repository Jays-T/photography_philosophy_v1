from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_total_on_save(sender, instance, created, **kwargs):
    """
    On lineitem create/update
    Update Order total
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_total_on_delete(sender, instance, **kwargs):
    """
    On lineItem delete
    Update Order total
    """
    instance.order.update_total()
