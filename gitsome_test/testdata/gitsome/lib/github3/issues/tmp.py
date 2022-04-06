from __future__ import unicode_literals

from json import dumps
from ..decorators import requires_auth
from ..models import GitHubCore


class Label(GitHubCore):
    def _update_attributes(self, label):
        reveal_type(label)