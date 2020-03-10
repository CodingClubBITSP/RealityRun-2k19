from .models import CustomUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_in


@receiver(user_logged_in, sender=CustomUser)
def login_check(sender, request, user, **kwargs):
    user.login_count += 1
    print('logged in')
    user.save()
    if user.login_count > 1:
        logout(request)
