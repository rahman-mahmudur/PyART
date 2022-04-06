from __future__ import unicode_literals

from ..models import GitHubCore
from ..users import User


class UserSearchResult(GitHubCore):
    def _update_attributes(self, data):
        reveal_type(result)