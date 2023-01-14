from django.conf import settings
from django.db import models
from autoslug import AutoSlugField

from books.models import Library


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.png', upload_to='profile_pictures')
    slug = AutoSlugField(populate_from='user')
    bio = models.CharField(max_length=255, blank=True)
    friends = models.ManyToManyField("Profile", blank=True)
    def get_absolute_url(self):
        return "/users/{}".format(self.slug)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    #TODO add timestamp




