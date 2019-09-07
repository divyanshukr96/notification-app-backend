import uuid
from Backend import settings
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    DEPARTMENT = 'DEPARTMENT'
    SOCIETY = 'SOCIETY'
    FACULTY = 'FACULTY'
    STUDENT = 'STUDENT'
    ADMIN = 'ADMIN'

    USER_TYPES = [
        (DEPARTMENT, 'Department'),
        (SOCIETY, 'Society'),
        (FACULTY, 'Faculty'),
        (STUDENT, 'Student'),
        (ADMIN, 'Admin'),

    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid5(uuid.NAMESPACE_DNS, settings.UUID_SECRET),
                          editable=False)

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    name = models.CharField(_('full name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    mobile = models.CharField(_('mobile'), max_length=15, blank=True)
    user_type = models.CharField(_('user type'), max_length=15, choices=USER_TYPES, default=STUDENT)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_admin = models.BooleanField(
        _('admin status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """Return the full name for the user."""
        return self.name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.name.split()[0].strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Student(User):
    pass