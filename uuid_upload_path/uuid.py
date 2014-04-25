from __future__ import absolute_import, unicode_literals

from uuid import uuid4
from base64 import urlsafe_b64encode


def uuid():
    return urlsafe_b64encode(uuid4().bytes).decode("ascii").rstrip("=")
