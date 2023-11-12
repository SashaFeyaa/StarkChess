from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, wallet_address, **extra_fields):
        """
        Create and save a user with the wallet_address.
        """
        if not wallet_address:
            raise ValueError(_("The wallet_address must be set"))

        user = self.model(wallet_address=wallet_address, **extra_fields)
        user.save()
        return user

    def create_superuser(self, wallet_address, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(wallet_address, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    wallet_address = models.CharField(unique=True, verbose_name='Wallet Address',
                                      max_length=100, null=False, blank=False)
    score = models.FloatField(default=0, verbose_name="User Score")
    registered = models.DateTimeField(auto_now_add=True, verbose_name="Registered")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # TODO: discuss nums for user pics
    profile_pic_num = models.IntegerField(default=0, verbose_name="User profile picture number")

    objects = CustomUserManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    USERNAME_FIELD = "wallet_address"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.wallet_address

    # add negative number if subtraction needed
    def add_points(self, point_amount):
        self.user_score += point_amount

    def get_tokens_for_user(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
