from __future__ import unicode_literals

from ..models import GitHubCore
from .commit import RepoCommit


class Comparison(GitHubCore):
    def _update_attributes(self, compare):
        reveal_type(compare)