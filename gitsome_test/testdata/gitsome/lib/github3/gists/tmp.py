from __future__ import unicode_literals

from ..models import GitHubCore


class GistFile(GitHubCore):


    def _update_attributes(self, attributes):
        reveal_type(attributes)