from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "savdo.apps.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            from savdo import apps
        except ImportError:
            pass
