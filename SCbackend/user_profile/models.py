from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractBaseUser):
    wallet_address = models.CharField(unique=True, verbose_name='Wallet Address',
                                      max_length=100, null=False, blank=False)
    score = models.FloatField(default=0, verbose_name="User Score")
    registered = models.DateTimeField(auto_now_add=True, verbose_name="Registered")

    # TODO: discuss nums for user pics
    profile_pic_num = models.IntegerField(default=0, verbose_name="User profile picture number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    USERNAME_FIELD = "wallet_address"
    REQUIRED_FIELDS = ["wallet_address"]

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
