from django.db import models

# Create your models here.UserProfile(Abs
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError('User must have mail')
        """normalize_email - This allow to normalize i.e it will take caps, smalls and treats same"""
        email = self.normalize_email(email)
        user = self.model(email=email, name = name)

        user.set_password(password)
        user.save(using=self._db)
        print('mod_user:', user)
        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff     = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Repesent own user profiles"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
       return self.name

    def get_short_name(self):
       return self.name

    def __str__(self):
       return self.email

class ProfileStatus(models.Model):

    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_tag  = models.CharField(max_length=120)
    status_text = models.TextField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_tag