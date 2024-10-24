from django.db import models
from ourblog import settings
from PIL import Image
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.manager import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(
        _(
            "first name",
        ),
        max_length=50,
    )
    last_name = models.CharField(
        _(
            "last name",
        ),
        max_length=50,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_profile"
    )
    email = models.EmailField(
        _("email address"),
        unique=True,
    )
    first_name = models.CharField(
        _(
            "first name",
        ),
        max_length=50,
    )
    last_name = models.CharField(
        _(
            "last name",
        ),
        max_length=50,
    )
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
