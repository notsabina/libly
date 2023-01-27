from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.db.models.signals import post_save

from books.models import Library


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default_profile.png", upload_to='profile_pictures')
    slug = AutoSlugField(populate_from='user')
    bio = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return "/users/{}".format(self.slug)

    def __str__(self):
        return self.user.username


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
