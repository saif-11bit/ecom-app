from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
# from rest_framework_simplejwt.tokens import RefreshToken
from helper.models import CommonBase


class UserManager(BaseUserManager):
    """
    Creates and saves user with given email and password
    """
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('User must have email')

        user = self.model(
            email=self.normalize_email(email,),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves superuser with given email and password
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, CommonBase):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
        db_index=True
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # we will add the profile photo here and other user fields
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh':str(refresh),
    #         'access':str(refresh.access_token),
    #     }
# No need for model account


class UserAddress(CommonBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=30)
    is_default = models.BooleanField(default=False)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street_add = models.TextField()
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.email}: {self.city} {self.state} {self.pin_code}"
