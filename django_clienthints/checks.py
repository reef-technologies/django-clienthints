from typing import Mapping, Sequence

from django.conf import settings
from django.core import checks


E001 = checks.Error(
    "Missing 'CLIENTHINTS' setting or it has wrong type.",
    hint="Has to be a list of valid Client Hints.",
    id='django_clienthints.E001',
)


E002 = checks.Error(
    "'CLIENTHINTS_ALLOWLISTS' setting has wrong type.",
    hint="Has to be a dict with feature as a key and a list of allowed sites, 'self' or '*' "
    "as a values (https://wicg.github.io/client-hints-infrastructure/#policy-controlled-features).",
    id='django_clienthints.E002',
)


def check_clienthints(app_configs, **kwargs):  # pragma: no cover
    config = getattr(settings, 'CLIENTHINTS', None)
    return [] if isinstance(config, Sequence) else [E001]


def check_clienthints_allowlist(app_configs, **kwargs):  # pragma: no cover
    config = getattr(settings, 'CLIENTHINTS_ALLOWLIST', None)
    if config is None:
        config = settings.CLIENTHINTS_ALLOWLIST = {}  # default value
    return [] if isinstance(config, Mapping) else [E002]
