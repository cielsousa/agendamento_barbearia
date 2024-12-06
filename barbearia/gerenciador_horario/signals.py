from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db import models
from .models import Monday
import threading
#from .tasks import reset_status_after_delay

def reset_status_after_delay(instance_id):
    try:
        instance = Monday.objects.get(id=instance_id)
        instance.scheduled = False
        
        instance.save()
    except Monday.DoesNotExist:
        pass  # Se a instância não for encontrada, podemos ignorar o erro.

"""
@receiver(post_save, sender=Monday)
def get_off_schedule(sender, instance):
    if instance.scheduled == True:
        threading.Timer(30, reset_status_after_delay, args=[instance.id]).start()
        #reset_status_after_delay.apply_async(args=[instance.id], countdown=600)
"""