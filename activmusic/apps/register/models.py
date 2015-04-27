# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UsernameLessUserManager(BaseUserManager):
    """
    A custom user manager that will handle a user model that doesn't have a username field.
    """

    def _create_user(self, email, is_superuser, password, **extra):
        """
        Factorized content of create_user() and create_superuser().
        """
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_superuser=is_superuser,
            is_staff=is_superuser,
            **extra
        )

        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password=None, **extra):
        """
        Create a regular user.
        """
        self._create_user(email, False, password, **extra)

    def create_superuser(self, email, password=None, **extra):
        """
        Create a super user.
        """
        self._create_user(email, True, password, **extra)

    def normalize_email(self, email):
        """
        Normalize an email address by putting it in lowercase. I fucking hate people that type
        uppercase emails [because emails are case-insensitive and uppercase is aggressive].
        """
        return email.lower()


class User(PermissionsMixin, AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    email = models.EmailField(unique=True, verbose_name=_('email'))
    first_name = models.CharField(max_length=100, verbose_name=_('firstname'))
    last_name = models.CharField(max_length=100, verbose_name=_('lastname'))
    is_staff = models.BooleanField(default=False, verbose_name=_('is staff'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('date joined'))

    objects = UsernameLessUserManager()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
