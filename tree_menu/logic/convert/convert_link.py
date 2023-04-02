from django.urls import NoReverseMatch, reverse
from django.conf import settings
import urllib.parse


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
