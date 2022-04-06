import collections
import functools

from requests.compat import urlparse, urlencode

from . import exceptions
from . import models


class GitHubIterator(models.GitHubCore, collections.Iterator):
    def __init__(self, count, url, cls, session, params=None, etag=None,
                 headers=None):
        models.GitHubCore.__init__(self, {}, session)
        self.original = count
        self.count = count
        self.url = url
        self.last_url = None
        self._api = self.url
        self.cls = cls
        self.params = params or {}
        self._remove_none(self.params)
        self.etag = None
        self.headers = headers or {}
        self.last_response = None
        self.last_status = 0

        if etag:
            reveal_type(self.headers)