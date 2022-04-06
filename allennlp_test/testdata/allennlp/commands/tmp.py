import argparse
import logging
import pathlib

from overrides import overrides
import torch

import allennlp
from allennlp.common.util import import_module_and_submodules
from allennlp.commands.subcommand import Subcommand
from allennlp.version import VERSION


logger = logging.getLogger(__name__)
reveal_type(Subcommand)