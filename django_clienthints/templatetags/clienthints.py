from django import template
from django.core.exceptions import ImproperlyConfigured
from django.utils.safestring import mark_safe

from ..utils import get_ch_accept_header_value


register = template.Library()


@register.simple_tag
def client_hints_meta(*args):
    client_hints = list(*args) or get_ch_accept_header_value()

    if not client_hints:
        raise ImproperlyConfigured(
            "Template tag 'client_hints_meta' is used but client hints "
            "are not provided as parameters nor via settings.CLIENTHINTS"
        )

    return mark_safe(f'<meta http-equiv="Accept-CH" content="{client_hints}">')
