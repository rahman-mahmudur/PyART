from __future__ import unicode_literals
from __future__ import print_function

from .githubcli import GitHubCli


def cli():
    github = GitHubCli()
    reveal_type(github)