from django.conf import settings


def get_ch_accept_header_value():
    if not settings.CLIENTHINTS:
        return ''

    return ','.join(settings.CLIENTHINTS)


def get_future_policy_header_value():
    if not settings.CLIENTHINTS_ALLOWLIST:
        return ''

    return ';'.join(
        f'{feature.lower()} {" ".join(allowlist)}'
        for feature, allowlist in settings.CLIENTHINTS_ALLOWLIST.items()
    )
