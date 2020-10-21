from django.apps import AppConfig
from django.core import checks
from django.utils.translation import ugettext_lazy as _

from .checks import check_clienthints, check_clienthints_allowlist


class ClientHintsConfig(AppConfig):  # pragma: no cover
    name = 'django_clienthints'
    verbose_name = _('Client Hints')

    def ready(self):
        checks.register(check_clienthints)
        checks.register(check_clienthints_allowlist)
