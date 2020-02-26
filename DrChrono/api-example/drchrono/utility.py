from social_django.models import UserSocialAuth
import collections


def get_token():
    """
    Social Auth module is configured to store our access tokens. This dark magic will fetch it for us if we've
    already signed in.
    """
    oauth_provider = UserSocialAuth.objects.get(provider='drchrono')
    access_token = oauth_provider.extra_data['access_token']
    return access_token

def convert_unicode_to_string(data):
    """
        converts a dict from unicode to string.
        input dict may have a list or str or another dict
    """
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert_unicode_to_string, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert_unicode_to_string, data))
    else:
        return data