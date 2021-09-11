"""
    loginpass.line
    ~~~~~~~~~~~~~~~~~~
    Loginpass Backend of LINE (line.me)
    Useful Links:
    - Dev Portal: https://developers.line.biz/
    - Before you can specify the email scope and ask the user for permission to obtain their email address, 
      you must first submit an application requesting access to users' email addresses
    - https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request
    :copyright: (c) 2021 by Jakee Indapanya
    :license: BSD, see LICENSE for more details.
"""

from ._core import map_profile_fields


def normalize_userinfo(client, data):
    return map_profile_fields(
        data, {"sub": "sub", "name": "name", "email": "email", "picture": "picture"}
    )


class LINE(object):
    NAME = "line"
    OAUTH_CONFIG = {
        "api_base_url": "https://access.line.me/v2",
        "access_token_url": "https://api.line.me/oauth2/v2.1/token",
        "authorize_url": "https://access.line.me/oauth2/v2.1/authorize",
        "userinfo_endpoint": "https://api.line.me/oauth2/v2.1/verify",
        "client_kwargs": {"scope": "profile openid email"},
        "userinfo_compliance_fix": normalize_userinfo,
    }
