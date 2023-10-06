from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    wallet_address = models.CharField(unique=True, verbose_name='Wallet Address', max_length=100)
    user_score = models.FloatField(default=0, verbose_name="User Score")
    registered = models.DateTimeField(auto_now_add=True, verbose_name="Registered")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    USERNAME_FIELD = "wallet_address"
    REQUIRED_FIELDS = ["wallet_address"]

    def __str__(self):
        return self.wallet_address

    # add negative number if subtraction needed
    def add_points(self, point_amount):
        self.user_score += point_amount

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
