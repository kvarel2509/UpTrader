import urllib.parse

from django.conf import settings
from django.urls import NoReverseMatch, reverse


class InvalidUrl(Exception):
    pass


def convert_link(link):
    netloc = urllib.parse.urlparse(link).netloc
    if netloc:
        return link
    try:
        return settings.CURRENT_DOMAIN + reverse(link)
    except NoReverseMatch:
        raise InvalidUrl()
