# from django.dispatch import Signal
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from .models import todo, UserActivity

# user_activity_signal = Signal(providing_args=["user", "action", "object"])


# @receiver(post_save, sender=todo)
# @receiver(post_delete, sender=todo)
# def user_activity_handler(sender, instance, **kwargs):
#     action = "Added" if kwargs.get("created") else "Updated"
#     user_activity_signal.send(sender=sender, user=instance.user, action=action, object=instance)

# @receiver(user_activity_signal)
# def save_user_activity(sender, user, action, object, **kwargs):
#     object_details = f"{object.__class__.__name__} - {object}"
#     UserActivity.objects.create(user=user, action=action, object_details=object_details)

